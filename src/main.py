from borrows import Borrows
import pandas as pd

if __name__ == '__main__':
    aave_borrows = Borrows("AAVE")
    compound_borrows = Borrows("COMPOUND")
    maker_borrows = Borrows("MAKER")
    cream_borrows = Borrows("CREAM")
    timestamp = 1612210494

    list_borrows = [*aave_borrows.get_borrows_from_timestamp(timestamp),
                    *compound_borrows.get_borrows_from_timestamp(timestamp),
                    *maker_borrows.get_borrows_from_timestamp(timestamp)
                    * cream_borrows.get_borrows_from_timestamp(timestamp)
                    ]

    df = pd.DataFrame.from_records(list_borrows)

    print(df[df.protocol == 'AAVE'].head())
    print(df[df.protocol == 'COMPOUND'].head())
    print(df[df.protocol == 'MAKER'].head())
    print(df[df.protocol == 'CREAM'].head())
