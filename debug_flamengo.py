import utils
import pandas as pd
import os

path = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input\API CARTOLA RODADA 1.xlsx"
df = utils.load_data(path)
fla = df[df['Time_Norm'] == 'FLAMENGO']
print(fla[['Data', 'Mand', 'Adversário']].head(20))
