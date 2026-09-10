# QuantAudit 🛡️

> **Your Backtest Passed. But Is It Valid?**

QuantAudit is an automated causal inspection engine designed for Quantitative Researchers and Developers. It automatically detects temporal leakage, lookahead bias, and statistical overfitting in Python backtesting pipelines before you risk real capital.

---

## ⚡ Quickstart

Install the package via `pip`:

```bash
pip install quantaudit
```

Audit your strategy file in just a few lines of Python:

```python
from quantaudit import AuditEngine

# Initialize the audit engine
engine = AuditEngine()

# Run a full structural check
report = engine.audit_file("examples/leaky_strategy.py")

# Display findings
print(report.summary())
```

---

## 🔍 What QuantAudit Catches

- ⏱️ **Temporal & Lookahead Bias:** Feature engineering executed before data split boundaries.
- 🔄 **Training-Data Reuse:** Improper reuse of training samples during parameter calibration.
- 📉 **Statistical Overfitting Checks:** Automated validation via CPCV, PBO, and Deflated Sharpe Ratio (DSR).

---

## 🤝 Free Backtest Audit Pilot

We are currently running a **Free Audit Pilot** for Quantitative Researchers. If you want to stress-test your backtest pipeline against 70+ failure scenarios without sharing proprietary alpha logic:

👉 **[Submit a Free Audit Request](https://tally.so/r/68lqB5)**
