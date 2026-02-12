import pandas as pd
import utils

path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\API CARTOLA RODADA 1.xlsx"
try:
    df = utils.load_data(path)
    if 'Posicao_Norm' in df.columns:
        print("Valores únicos em Posicao_Norm:", df['Posicao_Norm'].unique())
    if 'PosReal' in df.columns:
        print("Valores únicos em PosReal (raw):", df['PosReal'].unique())
    if 'Posicao' in df.columns:
        print("Valores únicos em Posicao (raw):", df['Posicao'].unique())
        
except Exception as e:
    print("Erro:", e)
