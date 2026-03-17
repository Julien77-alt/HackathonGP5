import pandas as pd
import numpy as np

file_path = "data/raw/HRDataset_v14.csv"
df = pd.read_csv(file_path)

print("\n Original Shape")
print(df.shape)

cols_to_remove = ["Employee_Name", "EmpID", "Email"]


cols_to_remove = [col for col in cols_to_remove if col in df.columns]
df = df.drop(columns=cols_to_remove)

print("\n Removed Columns")
print(cols_to_remove)

num_cols = df.select_dtypes(include=[np.number]).columns
cat_cols = df.select_dtypes(include=["object"]).columns

for col in num_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    if df[col].isnull().sum() > 0:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

print("\n Missing values after cleaning")
print(df.isnull().sum())

print("\n Final shape")
print(df.shape)

print("\n Final columns")
print(df.columns.tolist())

print("\n Sample data")
print(df.head())

output_path = "data/processed/cleaned_dataset.csv"
df.to_csv(output_path, index=False)

print(f"\n Cleaned dataset is saved at: {output_path}")