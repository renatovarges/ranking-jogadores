import utils
import pandas as pd
import os

def test_logic():
    print("=== INICIANDO VERIFICAÇÃO DE LÓGICA ===")
    
    # Paths
    base = r"c:\Users\User\.gemini\antigravity\scratch\Ranking jogadores\input"
    api_path = os.path.join(base, "API CARTOLA RODADA 1.xlsx")
    rodadas_path = os.path.join(base, "RODADAS_BRASILEIRAO_2026.txt")
    
    # 1. Load Data
    print(f"\n[1] Carregando dados de: {api_path}")
    df = utils.load_data(api_path)
    print(f"    Linhas carregadas: {len(df)}")
    if 'Data_dt' in df.columns:
        print("    Coluna Data_dt convertida com sucesso.")
        print("    Exemplos de datas:", df['Data_dt'].head(3).tolist())
    else:
        print("    ERRO: Data_dt não criada!")
        return

    # 2. Parse Rodadas
    print(f"\n[2] Processando Rodadas: {rodadas_path}")
    rodadas = utils.parse_rodadas(rodadas_path)
    print(f"    Times identificados: {len(rodadas)}")
    # Validar um time conhecido
    if 'FLAMENGO' in rodadas:
        print(f"    Flamengo prox jogos: {rodadas['FLAMENGO'][:2]}")
    else:
        print("    AVISO: Flamengo não encontrado nas rodadas.")

    # 3. Test Core Logic - TODAS
    print("\n[3] Testando Filtro 'Todas' (Últimos 3 Jogos)")
    # Escolher um time com bastante dados
    times = df['Time_Norm'].unique()
    test_time = 'FLAMENGO' if 'FLAMENGO' in times else times[0]
    print(f"    Time teste: {test_time}")
    
    ranking = utils.process_ranking(
        df, n_jogos=3, filter_type="Todas", target_round=1, 
        rodadas_data=rodadas, top_n_players=3, posicao_filter=None
    )
    
    if ranking:
        top1 = ranking[0]
        print(f"    Top 1 Geral: {top1['Nome']} ({top1['Posicao']}) - Pts: {top1['Total_Pontos']}")
        print(f"    Jogos considerados ({len(top1['Jogos'])}):")
        for j in top1['Jogos']:
            print(f"      - {j['Data']} | {j['Adversario']} | Pts: {j['Pontos']}")
            
        # Verificar ORDEM das datas
        dates = [j['Data'] for j in top1['Jogos']]
        if dates == sorted(dates, reverse=True):
            print("    SUCESSO: Jogos estão em ordem cronológica decrescente.")
        else:
            print("    ERRO: Jogos NÃO estão ordenados corretamente!")
    else:
        print("    Sem ranking 'Todas' gerado.")

    # 4. Test Core Logic - POR MANDO
    print("\n[4] Testando Filtro 'Por Mando' (Últimos 2 Jogos)")
    # Flamengo Rodada 1 = ?
    match_info = utils.get_next_match_info(test_time, rodadas, 1)
    if match_info:
        mando_target = match_info['mando']
        print(f"    Rodada 1 Flamengo é: {mando_target}")
        
        ranking_mando = utils.process_ranking(
             df, n_jogos=2, filter_type="Por Mando", target_round=1,
             rodadas_data=rodadas, top_n_players=3
        )
        
        if ranking_mando:
            top1_m = ranking_mando[0]
            player_team = top1_m['Time']
            print(f"    Top 1 Mando: {top1_m['Nome']} ({player_team}) - Pts: {top1_m['Total_Pontos']}")
            
            # Buscar mando deste time especifico
            p_next = utils.get_next_match_info(player_team, rodadas, 1)
            if p_next:
                p_target = p_next['mando']
                print(f"    Meta do {player_team}: {p_target}")
                
                for j in top1_m['Jogos']:
                    status_mando = "CASA" if j['Casa'] else "FORA"
                    match_ok = (status_mando == p_target)
                    print(f"      - {j['Data']} | {j['Adversario']} | {status_mando} | Match? {match_ok}")
            else:
                print(f"    Sem info de rodada para {player_team}")
        else:
            print("    Sem ranking 'Por Mando' gerado.")
    else:
        print("    Flamengo sem jogo na Rodada 1?")

    print("\n=== FIM DA VERIFICAÇÃO ===")

if __name__ == "__main__":
    test_logic()
