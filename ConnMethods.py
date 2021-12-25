import psycopg2 as pg
from database import PGDATABASE, PGHOST, PGPORT, PGUSER, PGPASSWORD
import pandas as pd


# conn = pg.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)

def df_from_table(tablename:str='results') -> pd.DataFrame:
    conn = pg.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)
    tabledata = pd.read_sql_query("SELECT uuid, start, stop, description, name, status FROM " + tablename, conn)
    return tabledata

def drop_table(tablename:str='tablename') -> None:
    conn = pg.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)
    cur = conn.cursor()

    delete_statement = f"DROP table {tablename};"
    cur.execute(delete_statement)

    # cur.commit()
    # cur.close()
    # conn.close()

if __name__ == "__main__":
    # print(df_from_table())
    drop_table('befores')