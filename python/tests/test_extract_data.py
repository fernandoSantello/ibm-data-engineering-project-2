import pandas as pd
from etl_modules.extract_data import extract

def test_extract():
    test_url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
    result = extract(test_url)

    assert isinstance(result, pd.DataFrame)
    assert not result.empty

    expected_columns = ['Rank', 'Bank name', 'Market cap (US$ billion)']
    for column in expected_columns:
        assert column in result.columns
