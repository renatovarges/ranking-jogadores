import streamlit as st
import pandas as pd
import os
import utils
import base64

# Configuração da Página
st.set_page_config(layout="wide", page_title="Ranking Cartola", page_icon="⚽")

# --- Autenticação ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    if st.session_state.authenticated:
        return True
    
    st.markdown("""
        <style>
        .stTextInput > div > div > input {
            text-align: center; 
            font-size: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        st.write("## 🔒 Acesso Restrito")
        placeholder = st.empty()
        pwd = placeholder.text_input("Digite o PIN de acesso:", type="password", key="login_pwd")
        
        if pwd:
            if pwd == "1979":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("🚫 PIN Incorreto")
    return False

if not check_password():
    st.stop()

# --- Helper Assets ---
def get_base64_encoded(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def render_custom_css():
    # Caminhos
    font_bold_path = os.path.join("assets", "fonts", "Decalotype-ExtraBold.otf")
    font_med_path = os.path.join("assets", "fonts", "Decalotype-Medium.otf")
    bg_path = os.path.join("assets", "logos", "background.png")
    
    font_bold_b64 = get_base64_encoded(font_bold_path)
    font_med_b64 = get_base64_encoded(font_med_path)
    bg_b64 = get_base64_encoded(bg_path)
    
    css = f"""
    /* Fonts Global import - scoped to report but needs to be global for fonts */
    @font-face {{
        font-family: 'Decalotype';
        src: url(data:font/otf;base64,{font_bold_b64}) format('opentype');
        font-weight: 800;
        font-style: normal;
    }}
    @font-face {{
        font-family: 'Decalotype';
        src: url(data:font/otf;base64,{font_med_b64}) format('opentype');
        font-weight: 500;
        font-style: normal;
    }}
    
    /* Scoped Styles for Report Only */
    .report-container {{
        font-family: 'Decalotype', sans-serif;
        width: 1200px; /* Fixed width for consistency */
        max-width: 1200px;
        margin: 0 auto;
        background-image: url(data:image/png;base64,{bg_b64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 50px 40px 40px 40px; 
        min-height: 1400px; /* Ensure minimum height */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        box-sizing: border-box;
        color: white;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }}
    
    /* ... Header Styles ... */

    /* Card Player */
    .player-card {{
        background-color: #14483A;
        border: 2px solid #1E7C5C;
        border-radius: 25px;
        padding: 20px 25px;
        margin-bottom: 25px;
        display: flex;
        align-items: flex-start; /* Safer than center for variable height */
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        position: relative;
        overflow: visible;
        height: auto;
    }}
    
    .card-left {{
        display: flex;
        align-items: center;
        margin-right: 20px; /* Replace gap */
        min-width: 380px;
        padding-top: 5px; /* Visual alignment with flex-start */
    }}
    
    /* ... */
    
    .card-right {{
        display: flex;
        flex-direction: column; 
        align-items: flex-end;
        width: 100%; 
        max-width: 65%; /* Restricting width to force predictable wrapping */
        box-sizing: border-box;
    }}
    
    .chips-row {{
        display: flex;
        flex-wrap: wrap; 
        justify-content: flex-end; 
        margin-bottom: 10px; /* Spacing between chips and scouts */
    }}
    
    .game-chip {{
        margin-left: 6px; /* Replace gap */
        margin-bottom: 6px;
        /* ... rest of chip styles ... */
    }}
    
    /* Total Scouts Bar */
    .scouts-bar {{
        background-color: #0f382e;
        padding: 8px 15px;
        border-radius: 12px;
        display: flex;
        flex-wrap: wrap; 
        width: auto; /* Let it shrink/grow */
        max-width: 100%;
        justify-content: flex-end;
        align-self: flex-end; /* Align to right */
    }}
    
    .scout-item, .scout-neg {{
        margin-left: 10px; /* Replace gap */
    }}

    /* Footer - Sticky at bottom */
    .tcc-footer {{
        background-color: #0f382e;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        margin-top: auto; /* Pushes to bottom */
        width: 100%;
        border-radius: 15px;
        box-sizing: border-box;
    }}
    
    /* Header Styles */
    .tcc-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }}
    
    .logo-box {{
        width: 160px;
        display: flex;
        justify-content: center;
    }}
    .logo-img {{
        width: 100%;
        height: auto;
    }}
    
    .title-box {{
        text-align: center;
        flex-grow: 1;
    }}
    
    .main-title-badge {{
        background-color: #0f382e;
        color: white;
        padding: 12px 50px;
        border-radius: 15px;
        font-size: 42px;
        font-weight: 800;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 25px;
        border: 2px solid #14483A;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }}
    
    .sub-title {{
        font-size: 32px;
        font-weight: 800;
        color: #0f382e;
        font-style: italic;
        text-transform: uppercase;
    }}
    
    .section-title {{
        font-size: 26px;
        font-weight: 800;
        color: black;
        text-align: center;
        margin: 100px 0 15px 0;
        font-style: italic;
        text-transform: uppercase;
    }}

    /* Card Player */
    .player-card {{
        background-color: #14483A;
        border: 2px solid #1E7C5C;
        border-radius: 25px;
        padding: 15px 25px 25px 25px; /* CORREÇÃO: Aumentado padding inferior de 15px para 25px */
        margin-bottom: 25px; /* CORREÇÃO: Aumentado de 15px para 25px */
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        position: relative; /* CORREÇÃO: Garante contenção dos elementos filhos */
        overflow: visible; /* CORREÇÃO: Permite que scouts bar seja visível */
    }}
    
    .card-left {{
        display: flex;
        align-items: center;
        gap: 25px;
        min-width: 400px;
    }}
    
    .player-circle {{
        width: 85px;
        height: 85px;
        background: white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 4px solid white;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(0,0,0,0.7);
    }}
    .player-circle img {{
        width: 95%;
        height: auto;
        object-fit: contain;
    }}
    
    .info-block h3 {{
        margin: 0;
        font-size: 28px;
        font-weight: 800;
        text-transform: uppercase;
        line-height: 1;
        color: white;
        font-family: 'Decalotype', sans-serif;
    }}
    
    .total-score {{
        font-size: 46px; 
        font-weight: 800;
        color: #2ecc71;
        line-height: 1;
        margin-top: 2px;
    }}
    
    .media-score {{
        font-size: 18px;
        color: #e5e7eb;
        font-weight: 500;
        margin-top: 5px;
        opacity: 0.9;
    }}
    
    .card-right {{
        display: flex;
        flex-direction: column; 
        align-items: flex-end;
        gap: 8px;
        max-width: 80%; /* CORREÇÃO ROBUSTA: Aumentado de 68% para 80% para evitar overflow */
        width: 100%; /* CORREÇÃO: Garante uso total do espaço disponível */
        box-sizing: border-box; /* CORREÇÃO: Inclui padding no cálculo */
    }}
    
    .chips-row {{
        display: flex;
        gap: 6px;
        flex-wrap: wrap; 
        justify-content: flex-end; 
        max-width: 1000px; 
    }}
    
    /* Chips */
    .game-chip {{
        border-radius: 50px;
        padding: 4px 10px;
        display: flex;
        align-items: center;
        gap: 8px;
        height: 48px; 
    }}
    
    .bg-casa {{ background-color: #ffe8cc; color: #333; }}
    .bg-fora {{ background-color: #dbeafe; color: #333; }}
    
    .chip-logo-circle {{
        width: 38px; 
        height: 38px;
        background-color: white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        flex-shrink: 0;
    }}
    
    .chip-adversario {{
        width: 95%;
        height: 95%;
        object-fit: contain;
    }}
    
    .chip-content {{
        display: flex;
        flex-direction: column; 
        justify-content: center;
        line-height: 1;
    }}

    .chip-score {{
        font-size: 19px;
        font-weight: 800;
        color: #111;
        white-space: nowrap; 
    }}
    
    .chip-scouts {{
        font-size: 14px;
        font-weight: 800;
        color: #333;
        white-space: nowrap;
    }}
    
    /* Total Scouts Bar */
    .scouts-bar {{
        background-color: #0f382e;
        padding: 6px 12px; /* CORREÇÃO: Reduzido padding lateral de 15px para 12px */
        border-radius: 12px;
        display: flex;
        flex-wrap: wrap; /* CORREÇÃO: Permite quebra de linha se necessário */
        gap: 8px; /* CORREÇÃO: Reduzido de 10px para 8px para melhor ajuste */
        margin-top: 8px;
        width: 100%; /* CORREÇÃO ROBUSTA: Força largura total do container pai */
        max-width: 100%; /* CORREÇÃO: Garante que não ultrapasse o card */
        box-sizing: border-box; /* CORREÇÃO: Inclui padding no cálculo de largura */
        justify-content: flex-end; /* CORREÇÃO: Alinha à direita como chips */
    }}
    
    .scout-item {{
        font-size: 15px;
        font-weight: 700;
        color: #00e676; 
    }}
    .scout-neg {{ 
        font-size: 15px;
        font-weight: 700;
        color: #ff5252; 
    }} 
    
    /* Scoped colors for inside chips too */
    .chip-scout-pos {{ color: #008f4c; }} 
    
    /* Footer */
    .tcc-footer {{
        background-color: #0f382e;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 15px;
        margin-top: 40px; /* CORREÇÃO ROBUSTA: Reduzido de 160px para 40px */
        border-radius: 0 0 15px 15px;
        position: relative;
    }}
    .footer-content {{
         display: flex;
         align-items: center;
         gap: 20px;
    }}
    .footer-text {{
        font-size: 16px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .footer-logo {{
        height: 40px;
        width: auto;
    }}
    
    """
    return css

# --- Logic ---

def get_team_logo_path(team_name):
    normalized = utils.normalize_name(team_name).lower().replace(" ", "_")
    mapa = {
        "atletico_go": "atletico_goianiense", 
        "athletico": "athletico_pr",
        "red_bull": "red_bull_bragantino",
        "bragantino": "red_bull_bragantino",
        "atletico-mg": "atletico_mg"
    }
    filename = f"{normalized}.png"
    path = os.path.join("assets/teams", filename)
    if os.path.exists(path): return path
    for k, v in mapa.items():
        if k in normalized:
            path = os.path.join("assets/teams", f"{v}.png")
            if os.path.exists(path): return path
    return None

def img_to_b64(img_path):
    if not img_path: return ""
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def sort_scouts(scouts_dict):
    """
    Sort scouts: 
    1. Positive scouts (Desc quantity)
    2. Negative scouts (Desc quantity)
    """
    neg_keys = ['GS', 'PP', 'FC', 'I', 'PI', 'CA', 'CV', 'PC', 'GC']
    
    pos_list = []
    neg_list = []
    
    for k, v in scouts_dict.items():
        if v == 0: continue
        if k in neg_keys:
            neg_list.append((k, v))
        else:
            pos_list.append((k, v))
            
    pos_list.sort(key=lambda x: x[1], reverse=True)
    neg_list.sort(key=lambda x: x[1], reverse=True)
    
    return pos_list, neg_list

def render_full_report_dual(position, rodada, players_mando, players_geral, n_jogos):
    logo_tcc_path = os.path.join("assets", "logos", "logo_tcc.png")
    logo_white_path = os.path.join("assets", "logos", "logo_tcc_branco.png")
    
    logo_b64 = img_to_b64(logo_tcc_path) if os.path.exists(logo_tcc_path) else ""
    logo_white_b64 = img_to_b64(logo_white_path) if os.path.exists(logo_white_path) else ""
    
    css = render_custom_css()
    
    logo_img_tag = f'<img src="data:image/png;base64,{logo_b64}" class="logo-img"/>' if logo_b64 else ''
    footer_logo_tag = f'<img src="data:image/png;base64,{logo_white_b64}" class="footer-logo"/>' if logo_white_b64 else ''
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Ranking {position} - Rodada {rodada}</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/html-to-image/1.11.11/html-to-image.min.js"></script>
        <style>
            body {{ margin: 0; padding: 0; background-color: #f0f2f6; }}
            {css}
            
            #btn-download {{
                position: fixed;
                top: 20px;
                right: 20px;
                background-color: #1E7C5C;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-family: sans-serif;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                z-index: 9999;
                transition: all 0.3s ease;
            }}
            #btn-download:hover {{
                background-color: #14483A;
                transform: scale(1.05);
            }}
        </style>
    </head>
    <body>
    <button id="btn-download" onclick="downloadPNG()">📸 BAIXAR ARTE (NOVO MOTOR)</button>
    
    <script>
        async function downloadPNG() {{
            const btn = document.getElementById('btn-download');
            const element = document.querySelector('.report-container');
            const originalText = btn.innerText;

            btn.innerText = "⏳ Processando...";
            btn.disabled = true;
            
            // Force layout recalc
            await document.fonts.ready;
            
            // Fixed dimensions for consistent rendering
            const targetWidth = 1200;
            
            const config = {{
                quality: 1.0,
                width: targetWidth,
                height: element.offsetHeight + 5, // Exact height capture
                style: {{
                    'transform': 'none',
                    'margin': '0',
                    'width': '1200px', // Force width in render
                    'min-height': '1400px' // Ensure background covers
                }},
                cacheBust: true,
            }};

            try {{
                // 1.5x scale is usually sufficient and stable
                const dataUrl = await htmlToImage.toPng(element, {{ ...config, pixelRatio: 1.5 }});
                
                const link = document.createElement('a');
                link.download = `Ranking_{position}_{rodada}.png`;
                link.href = dataUrl;
                link.click();
                
            }} catch (err) {{
                console.error("Erro:", err);
                alert("Erro ao gerar imagem. Tente novamente.");
            }} finally {{
                btn.innerText = originalText;
                btn.disabled = false;
            }}
        }}
    </script>
    <div class="report-container">
        <div class="tcc-header">
            <div class="logo-box">{logo_img_tag}</div>
            <div class="title-box">
                <div class="main-title-badge">RANKING POR POSIÇÃO</div>
                <div class="sub-title">{position}S - RODADA {rodada}</div>
            </div>
            <div class="logo-box">{logo_img_tag}</div>
        </div>
        
        <div style="display: flex; justify-content: flex-end; gap: 20px; margin-bottom: -10px; margin-top: 50px; max-width: 1000px; margin-left: auto; margin-right: auto; padding-right: 15px; position: relative; z-index: 10;">
            <div style="display: flex; align-items: center; gap: 6px;">
                <div style="width: 16px; height: 16px; background-color: #ffe8cc; border-radius: 50%; border: 1px solid #ccc;"></div>
                <span style="font-weight: bold; color: #333; font-size: 14px;">CASA</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px;">
                <div style="width: 16px; height: 16px; background-color: #dbeafe; border-radius: 50%; border: 1px solid #ccc;"></div>
                <span style="font-weight: bold; color: #333; font-size: 14px;">FORA</span>
            </div>
        </div>
        
        <div class="section-title" style="margin-top: 0px;">Últimos {n_jogos} jogos por mando</div>
    """
    
    def render_cards(players):
        cards_html = ""
        for i, p in enumerate(players):
            nome = p['Nome']
            time = p['Time']
            pts = f"{p['Total_Pontos']:.2f}"
            media = f"{p.get('Media_Pontos', 0):.2f}"
            basica = f"{p.get('Media_Basica', 0):.2f}"
            
            team_logo = get_team_logo_path(time)
            team_b64 = img_to_b64(team_logo)
            
            chips_content = ""
            for jogo in p['Jogos']:
                bg_class = "bg-casa" if jogo['Casa'] else "bg-fora"
                opp_logo = get_team_logo_path(jogo['Adversario'])
                opp_b64 = img_to_b64(opp_logo)
                
                pos_s, neg_s = sort_scouts(jogo['Scouts'])
                
                txt_list = [f"{v}{k}" for k,v in pos_s] + [f"{v}{k}" for k,v in neg_s]
                scouts_final = " ".join(txt_list)
                
                opp_img_tag = f'<img src="data:image/png;base64,{opp_b64}" class="chip-adversario"/>' if opp_b64 else ''
                opp_wrapper = f'<div class="chip-logo-circle">{opp_img_tag}</div>' if opp_b64 else ''
                
                score_val = jogo['Pontos']
                score_str = f"{score_val:.2f}"
                
                chips_content += f"""
                <div class="game-chip {bg_class}">
                    {opp_wrapper}
                    <div class="chip-content">
                        <div class="chip-score">{score_str} &mdash; {scouts_final}</div>
                    </div>
                </div>
                """
            
            t_pos, t_neg = sort_scouts(p['Scouts'])
            
            rendered_scouts = []
            for k, v in t_pos:
                rendered_scouts.append(f'<span class="scout-item">{v}{k}</span>')
            for k, v in t_neg:
                rendered_scouts.append(f'<span class="scout-neg">{v}{k}</span>')
            
            total_scouts_html = " ".join(rendered_scouts) 
            
            cards_html += f"""
            <div class="player-card">
                <div class="card-left">
                    <div class="player-circle">
                         {'<img src="data:image/png;base64,' + team_b64 + '"/>' if team_b64 else ''}
                    </div>
                    <div class="info-block">
                        <h3>{i+1}. {nome}</h3>
                        <div class="total-score">{pts}</div>
                        <div class="media-score">Média: {media} | Básica: {basica}</div>
                    </div>
                </div>
                <div class="card-right">
                    <div class="chips-row">
                        {chips_content}
                    </div>
                    <div class="scouts-bar">
                        {total_scouts_html}
                    </div>
                </div>
            </div>
            """
        return cards_html

    html += render_cards(players_mando)
    
    html += f"""
        <div class="section-title">Últimos {n_jogos} jogos gerais</div>
    """
    
    html += render_cards(players_geral)
    
    html += f"""
        <div class="tcc-footer">
            <div class="footer-content">
                {footer_logo_tag}
                <div class="footer-text">MATERIAL EXCLUSIVO &ndash; TREINANDO CAMPEÕES DE CARTOLA</div>
            </div>
        </div>
    </div>
    </body>
    </html>
    """
    return html

# --- App Layout ---
st.markdown(f"<style>{render_custom_css()}</style>", unsafe_allow_html=True)
st.title("Geração de Rankings (Modo Arte Final)")

DEFAULT_RODADAS = os.path.join("input", "RODADAS_BRASILEIRAO_2026.txt")
DEFAULT_CLASSIF_XLSX = os.path.join("input", "DIVISÃO VOLANTES E MEIAS.xlsx")
DEFAULT_CLASSIF_CSV = os.path.join("input", "classificacao_meias_volantes.csv")

with st.sidebar:
    st.header("1. Upload de Dados")
    uploaded_api = st.file_uploader("Planilha API (Excel)", type=["xlsx"])
    
    has_rodadas = os.path.exists(DEFAULT_RODADAS)
    uploaded_rodadas = None if has_rodadas else st.file_uploader("Rodadas (TXT)", type=["txt"])
    if has_rodadas: st.success("✅ Rodadas identificado")
    
    has_classif = os.path.exists(DEFAULT_CLASSIF_XLSX) or os.path.exists(DEFAULT_CLASSIF_CSV)
    uploaded_classif = None if has_classif else st.file_uploader("Classif. Meias/Volantes", type=["csv", "xlsx"])
    if has_classif: st.success("✅ Classificação identificado")
    
    st.divider()
    st.header("2. Configuração")
    n_jogos = st.number_input("Últimos N Jogos", 1, 10, 3)
    rodada_ref = st.number_input("Rodada Atual (Referência)", 1, 38, 2)
    top_n = st.number_input("Top Jogadores", 1, 20, 5)
    filtro_pos = st.selectbox("Posição", ["Todas", "Goleiro", "Lateral", "Zagueiro", "Volante", "Meia", "Atacante"])
    
    btn_run = st.button("GERAR ARTES", type="primary")

if btn_run and uploaded_api:
    with st.spinner("Gerando arte dupla..."):
        df = utils.load_data(uploaded_api)
        
        rodadas_data = {}
        if uploaded_rodadas:
             with open("temp_r.txt", "wb") as f: f.write(uploaded_rodadas.getbuffer())
             rodadas_data = utils.parse_rodadas("temp_r.txt")
        elif has_rodadas:
             rodadas_data = utils.parse_rodadas(DEFAULT_RODADAS)
             
        pos_map = {}
        target_c = None
        if uploaded_classif:
            ext = uploaded_classif.name.split('.')[-1]
            target_c = f"temp_c.{ext}"
            with open(target_c, "wb") as f: f.write(uploaded_classif.getbuffer())
        elif has_classif:
            target_c = DEFAULT_CLASSIF_XLSX if os.path.exists(DEFAULT_CLASSIF_XLSX) else DEFAULT_CLASSIF_CSV
        
        if target_c:
             if os.path.exists(target_c):
                pos_map = utils.load_classificacao(target_c)
             if not pos_map and os.path.exists(DEFAULT_CLASSIF_CSV) and target_c != DEFAULT_CLASSIF_CSV:
                 pos_map = utils.load_classificacao(DEFAULT_CLASSIF_CSV)

        positions = [filtro_pos] if filtro_pos != "Todas" else ['Goleiro', 'Lateral', 'Zagueiro', 'Volante', 'Meia', 'Atacante']
        
        for pos in positions:
            filter_p = [pos]
            if pos == 'Lateral': filter_p = ['Lateral', 'Lat']
            if pos == 'Zagueiro': filter_p = ['Zagueiro', 'Zag']
            
            rank_mando = utils.process_ranking(df, n_jogos, "Por Mando", rodada_ref, rodadas_data, top_n, filter_p, pos_map)
            rank_geral = utils.process_ranking(df, n_jogos, "Todas", rodada_ref, rodadas_data, top_n, filter_p, pos_map)
            
            if not rank_mando and not rank_geral:
                st.warning(f"Sem dados para {pos}")
                continue
                
            full_html = render_full_report_dual(pos.upper(), rodada_ref, rank_mando, rank_geral, n_jogos)
            
            st.subheader(f"🎨 Resultado: {pos}")
            st.components.v1.html(full_html, height=1200, scrolling=True)
            
            b64_html = base64.b64encode(full_html.encode("utf-8")).decode()
            href = f'<a href="data:text/html;base64,{b64_html}" download="Ranking_{pos}_{rodada_ref}.html" style="padding:15px; background: #1E7C5C; color:white; text-decoration:none; border-radius:8px; font-weight:bold; display:block; text-align:center;">📥 BAIXAR ARTE {pos.upper()} (HTML)</a>'
            st.markdown(href, unsafe_allow_html=True)

elif btn_run and not uploaded_api:
    st.error("⚠️ Necessário fazer upload da Planilha API.")

