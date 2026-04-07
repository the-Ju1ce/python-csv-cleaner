import pandas as pd

# Load CSV
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove blank rows
df = df.dropna(how="all")

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(df)

print("\nDone! File saved as cleaned_data.csv")
