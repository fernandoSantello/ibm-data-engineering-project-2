import pandas as pd
import numpy as np
import tempfile
from etl_modules.transform_data import transform

def test_transform_adds_correct_columns():
    df_mock = pd.DataFrame({'Market cap (US$ billion)': [100, 200, 300]})
    df_rates_mock = pd.DataFrame({'Currency': ['EUR', 'GBP', 'INR'], 'Rate': [0.85, 0.75, 75]})
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        df_rates_mock.to_csv(tmp.name, index=False)
        transformed_df = transform(df_mock, tmp.name)
        expected_columns = ['MC_USD_Billion', 'MC_EUR_Billion', 'MC_GBP_Billion', 'MC_INR_Billion']
        assert all(column in transformed_df.columns for column in expected_columns)
        
        np.testing.assert_array_almost_equal(
            transformed_df['MC_EUR_Billion'],
            df_mock['Market cap (US$ billion)'] * 0.85
        )
