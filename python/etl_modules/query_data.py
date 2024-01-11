import pandas as pd
from sqlalchemy import Engine


def run_query(engine: Engine, statment: str) -> pd.DataFrame:
    query_output = pd.read_sql(statment, engine)
    print(query_output)
    return query_output
