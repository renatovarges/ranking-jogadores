import pandas as pd
path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\DIVISÃO VOLANTES E MEIAS.xlsx"
df = pd.read_excel(path, header=None)

print("Scanning first 50 rows for any data in cols > 2...")
for i, row in df.head(50).iterrows():
    # Get values from col index 3 onwards
    vals = row.iloc[3:].values
    # Check if any is not null
    not_na = [x for x in vals if pd.notna(x)]
    if not_na:
        print(f"Row {i} has data: {not_na}")
        print(row.to_dict())
