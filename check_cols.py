import pandas as pd
import os

path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\API CARTOLA RODADA 1.xlsx"
try:
    df = pd.read_excel(path, sheet_name='Por jogo', nrows=1)
    print("COLUNAS POR JOGO:", list(df.columns))
except Exception as e:
    print("Erro:", e)
