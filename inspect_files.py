import pandas as pd
import os

base_path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores"
input_path = os.path.join(base_path, "input")

files = {
    "api": os.path.join(input_path, "API CARTOLA RODADA 1.xlsx"),
    "divisao": os.path.join(input_path, "DIVISÃO VOLANTES E MEIAS.xlsx"),
    "classificacao_csv": os.path.join(input_path, "classificacao_meias_volantes.csv"),
    "rodadas": os.path.join(input_path, "RODADAS_BRASILEIRAO_2026.txt")
}

def inspect_excel(path, name):
    print(f"\n--- Inspecting {name} ---")
    try:
        # Load all sheets to see structure
        xl = pd.ExcelFile(path)
        print(f"Sheets: {xl.sheet_names}")
        for sheet in xl.sheet_names:
            print(f"Sheet: {sheet}")
            df = pd.read_excel(path, sheet_name=sheet, nrows=5)
            print("Columns:", list(df.columns))
            # print("First row sample:", df.iloc[0].to_dict() if not df.empty else "Empty")
    except Exception as e:
        print(f"Error reading {name}: {e}")

def inspect_csv(path, name):
    print(f"\n--- Inspecting {name} ---")
    try:
        df = pd.read_csv(path, nrows=5, sep=None, engine='python') # Auto-detect separator
        print("Columns:", list(df.columns))
        print("First row:", df.iloc[0].to_dict() if not df.empty else "Empty")
    except Exception as e:
        print(f"Error reading {name}: {e}")

def inspect_text(path, name):
    print(f"\n--- Inspecting {name} ---")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            print(f.read(500))
    except Exception as e:
        try:
            with open(path, 'r', encoding='latin-1') as f:
                print(f.read(500))
        except Exception as e2:
            print(f"Error reading {name}: {e2}")

inspect_excel(files["api"], "API Cartola")
inspect_excel(files["divisao"], "Divisao Volantes/Meias")
inspect_csv(files["classificacao_csv"], "Classificacao CSV")
inspect_text(files["rodadas"], "Rodadas TXT")
