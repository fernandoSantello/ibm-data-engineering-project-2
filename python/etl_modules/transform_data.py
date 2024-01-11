import pandas as pd
import numpy as np

def transform(df: pd.DataFrame, rates_file_path: str) -> pd.DataFrame:
    df_rates = pd.read_csv(rates_file_path)
    df = df.rename(columns={'Market cap (US$ billion)': 'MC_USD_Billion'})
    eur_value = float(df_rates.loc[df_rates['Currency'] == 'EUR', 'Rate'].iloc[0])
    gbp_value = float(df_rates.loc[df_rates['Currency'] == 'GBP', 'Rate'].iloc[0])
    inr_value = float(df_rates.loc[df_rates['Currency'] == 'INR', 'Rate'].iloc[0])
    df['MC_EUR_Billion'] = np.round(df['MC_USD_Billion'] * eur_value, 2)
    df['MC_GBP_Billion'] = np.round(df['MC_USD_Billion'] * gbp_value, 2)
    df['MC_INR_Billion'] = np.round(df['MC_USD_Billion'] * inr_value, 2)
    return df
