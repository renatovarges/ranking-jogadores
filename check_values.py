import pandas as pd
import os

path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\API CARTOLA RODADA 1.xlsx"
try:
    df = pd.read_excel(path, sheet_name='Por jogo')
    print("Valores únicos em 'Mand':", df['Mand'].unique())
    print("Amostra das primeiras 5 linhas de Mand:", df['Mand'].head(5).tolist())
except Exception as e:
    print("Erro:", e)
