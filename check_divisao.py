import pandas as pd
import os

path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\DIVISÃO VOLANTES E MEIAS.xlsx"
try:
    df = pd.read_excel(path)
    print("Colunas Divisão:", list(df.columns))
    print("Amostra:", df.head(5).to_dict(orient='records'))
except Exception as e:
    print("Erro:", e)
