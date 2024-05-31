import pandas as pd
import heapq
from scipy.spatial.distance import cosine


def replace_nan_with_not_available(df):
  # Iterate through rows (using index for efficiency)
  for i in df.index:
    # Check if any element in the row is NaN
    if df.iloc[i].isna().any():
      # Replace all NaN values in the row with "not available"
      df.iloc[i] = df.iloc[i].fillna('not available')
  return df
