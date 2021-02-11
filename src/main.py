from borrows import Borrows
import pandas as pd

if __name__ == '__main__':
    aave_borrows = Borrows("AAVE")
    compound_borrows = Borrows("COMPOUND")
    timestamp = 1612210494

    list_borrows = [*aave_borrows.get_borrows_from_timestamp(timestamp),
                    *compound_borrows.get_borrows_from_timestamp(timestamp)]

    df = pd.DataFrame.from_records(list_borrows)

    print(df[df.protocol == 'AAVE'].head())
    print(df[df.protocol == 'COMPOUND'].head())
