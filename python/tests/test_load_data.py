import tempfile
import os
import pandas as pd
from etl_modules.load_data import load_to_csv, load_to_db
import pytest
import sqlite3

def test_load_to_csv_creates_file():
    with tempfile.TemporaryDirectory() as tmpdirname:
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        file_path = os.path.join(tmpdirname, 'test.csv')
        load_to_csv(df, file_path)
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) > 0

@pytest.fixture
def db_connection():
    con = sqlite3.connect(":memory:")
    yield con
    con.close()

def test_load_to_db(db_connection):
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    table_name = 'test_table'
    load_to_db(table_name, df, db_connection)
    loaded_df = pd.read_sql_query(f"SELECT * FROM {table_name}", db_connection)
    pd.testing.assert_frame_equal(df, loaded_df)
    