# Example of a clean strategy with proper train/test isolation
import pandas as pd
from sklearn.preprocessing import StandardScaler

def run_backtest(df):
    train = df.iloc[:1000].copy()
    test = df.iloc[1000:].copy()
    
    # ✅ CLEAN: Fit scaler ONLY on training data, then transform both
    scaler = StandardScaler()
    train["scaled_feature"] = scaler.fit_transform(train[["close"]])
    test["scaled_feature"] = scaler.transform(test[["close"]])
    
    return train, test
