import pandas as pd

def create_lag_features(df)
       
    df['Inflation_Lag1'] = df.groupby('country_name')['Inflation '].shift(1)
    df['Inflation_Lag2'] = df.groupby('country_name')['Inflation (CPI %)'].shift(2)

    df['gdp_growth_Lag1'] = df.groupby('country_name')['GDP']