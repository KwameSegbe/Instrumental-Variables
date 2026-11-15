# Import packages
import pandas as pd
import wooldridge as woo
import statsmodels.api as sm
from linearmodels.iv import IV2SLS

# 1. Load the 401(k) dataset
df = woo.data("401ksubs")

print("Dataset shape:")
print(df.shape)

from pathlib import Path

# Create a "data" folder next to code.py (if it doesn't already exist)
data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)

# Save the dataset
df.to_csv(data_dir / "401ksubs.csv", index=False)

print("Saved to:", data_dir / "401ksubs.csv")