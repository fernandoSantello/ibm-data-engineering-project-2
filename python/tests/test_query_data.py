import pandas as pd
import pytest
import sqlite3
from etl_modules.query_data import run_query 

@pytest.fixture
def db_engine():
    con = sqlite3.connect(":memory:")
    engine = con
    yield engine
    con.close()

def test_run_query_returns_dataframe(db_engine):
    db_engine.execute("CREATE TABLE test_table (id INTEGER, name TEXT)")
    db_engine.execute("INSERT INTO test_table (id, name) VALUES (1, 'Test')")
    query = "SELECT * FROM test_table"
    result_df = run_query(db_engine, query)
    assert isinstance(result_df, pd.DataFrame)
    assert not result_df.empty
    assert result_df.iloc[0]['id'] == 1
    assert result_df.iloc[0]['name'] == 'Test'
