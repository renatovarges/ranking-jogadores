
import pandas as pd
import utils
import os

def get_team_logo_path_sim(team_name):
    normalized = utils.normalize_name(team_name).lower().replace(" ", "_")
    mapa = {
        "atletico_go": "atletico_goianiense", 
        "athletico": "athletico_pr",
        "red_bull": "red_bull_bragantino",
        "bragantino": "red_bull_bragantino"
    }
    filename = f"{normalized}.png"
    # Mocking os.path.join and exists for simulation
    expected_path = f"assets/teams/{filename}"
    
    # We know atletico_mg.png exists but others might not in this script context if we don't check filesystem
    # But let's just use the logic from app.py
    
    # Actually, let's just use the exact logic, assuming running from root
    path = os.path.join("assets/teams", filename)
    if os.path.exists(path): return path
    for k, v in mapa.items():
        if k in normalized:
            path = os.path.join("assets/teams", f"{v}.png")
            if os.path.exists(path): return path
    return None

def check_teams():
    # Load data
    file_path = os.path.join("input", "API CARTOLA RODADA 1.xlsx")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        df = pd.read_excel(file_path)
        # Assuming 'Clube' or similar column holds team names. Let's inspect columns first or valid based on utils.load_data
        # utils.load_data might rename columns. Let's assume standard pandas read for now.
        print("Columns:", df.columns)
        
        # Look for team column
        team_col = None
        for col in df.columns:
            if "clube" in col.lower() or "time" in col.lower():
                team_col = col
                break
        
        if team_col:
            teams = df[team_col].dropna().unique()
            print(f"Found teams in column '{team_col}':")
            for team in teams:
                path = get_team_logo_path_sim(team)
                status = "✅ Found" if path else "❌ Missing"
                print(f"{team} -> {path} ({status})")
        else:
            print("Could not identify team column.")
            
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    check_teams()
