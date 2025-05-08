import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "Sample-1m.parquet")
df = pd.read_parquet(file_path)
print(f"Number of records: {len(df)}")
