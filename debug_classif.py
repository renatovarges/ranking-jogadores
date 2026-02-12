import utils
import pandas as pd
import os

path_xlsx = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\DIVISÃO VOLANTES E MEIAS.xlsx"
path_csv = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\classificacao_meias_volantes.csv"

print("--- Testing XLSX Load ---")
map_xlsx = utils.load_classificacao(path_xlsx)
print(f"Loaded {len(map_xlsx)} entries from XLSX")
volantes_xlsx = {k: v for k, v in map_xlsx.items() if 'VOLANTE' in str(v).upper()}
print(f"Found {len(volantes_xlsx)} VOLANTES in XLSX. Sample: {list(volantes_xlsx.items())[:5]}")

print("\n--- Testing CSV Load ---")
map_csv = utils.load_classificacao(path_csv)
print(f"Loaded {len(map_csv)} entries from CSV")
volantes_csv = {k: v for k, v in map_csv.items() if 'VOLANTE' in str(v).upper()}
print(f"Found {len(volantes_csv)} VOLANTES in CSV. Sample: {list(volantes_csv.items())[:5]}")
