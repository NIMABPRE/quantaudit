# Example of a leaky strategy where feature scaling happens before split
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run_backtest(df):
    # ❌ LEAK: Scaling whole dataset before train/test split
    scaler = StandardScaler()
    df["scaled_feature"] = scaler.fit_transform(df[["close"]])
    
    train = df.iloc[:1000]
    test = df.iloc[1000:]
    return train, test
