import pandas as pd
import sqlite3 as db

def load_to_csv(df: pd.DataFrame, save_csv_path: str) -> None:
    df.to_csv(save_csv_path)

def load_to_db(table_name: str, df: pd.DataFrame, con: db.Connection) -> None:
    df.to_sql(name=table_name, con=con, if_exists='replace', index=False)
    