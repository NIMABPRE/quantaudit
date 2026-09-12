# QuantAudit Challenge: A strategy with apparent Sharpe of 3.8 hiding subtle temporal leaks.
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def run_backtest_pipeline(df):
    # Leak 1: Global scaling before split
    scaler = StandardScaler()
    df["scaled_close"] = scaler.fit_transform(df[["close"]])
    
    # Leak 2: Future target leakage via negative shift
    df["future_return"] = df["close"].shift(-1) / df["close"] - 1
    
    # Leak 3: Lookahead in rolling window
    df["signal"] = df["scaled_close"].rolling(10).mean()
    
    train = df.iloc[:1000].copy()
    test = df.iloc[1000:].copy()
    return train, test
