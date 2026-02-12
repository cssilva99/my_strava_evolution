import requests
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO FINAL (Sem links!) ---
CLIENT_ID = '197799'
CLIENT_SECRET = '3019d7e204a6d8eef25460977f5a50e001b78503'
REFRESH_TOKEN = 'a0bff0bddada6d84eacc61310b13d93ba3895bd5'

def analise_claudia_2025():
    # 1. Autenticação Automática
    res = requests.post("https://www.strava.com/oauth/token", data={
        'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN, 'grant_type': 'refresh_token'
    }).json()
    
    token = res['access_token']
    
    # 2. Obter dados de 2025
    headers = {'Authorization': f'Bearer {token}'}
    data = requests.get("https://www.strava.com/api/v3/athlete/activities", 
                        headers=headers, params={'per_page': 100}).json()
    
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['start_date_local'])
    df = df[df['Data'] >= '2025-01-01'].sort_values('Data')

    # 3. Gerar os Gráficos um por um
    modalidades = [('Run', 'Corrida'), ('Swim', 'Natação'), ('Ride', 'Ciclismo')]

    for tipo, nome in modalidades:
        sub = df[df['type'] == tipo].copy()
        if sub.empty: continue

        print(f"\n{'='*10} {nome.upper()} {'='*10}")

        # --- PACE / VELOCIDADE ---
        plt.figure(figsize=(10, 4))
        if tipo == 'Run':
            sub['M'] = (sub['moving_time'] / 60) / (sub['distance'] / 1000)
            plt.plot(sub['Data'], sub['M'], 'bo-', label='Pace')
            plt.gca().invert_yaxis()
            plt.title(f"{nome}: Evolução do Pace (min/km)")
        elif tipo == 'Swim':
            sub['M'] = (sub['moving_time'] / 60) / (sub['distance'] / 100)
            plt.plot(sub['Data'], sub['M'], 'bo-', label='Pace')
            plt.gca().invert_yaxis()
            plt.title(f"{nome}: Evolução do Pace (min/100m)")
        else:
            sub['M'] = (sub['distance'] / 1000) / (sub['moving_time'] / 3600)
            plt.plot(sub['Data'], sub['M'], 'go-', label='Velocidade')
            plt.title(f"{nome}: Evolução da Velocidade (km/h)")
        plt.grid(True, alpha=0.3); plt.show()

        # --- HR MÉDIO ---
        if 'average_heartrate' in sub.columns:
            plt.figure(figsize=(10, 4))
            plt.plot(sub['Data'], sub['average_heartrate'], 'ro-')
            plt.title(f"{nome}: Heart Rate Médio (BPM)")
            plt.grid(True, alpha=0.3); plt.show()

        # --- HR MÁXIMO ---
        if 'max_heartrate' in sub.columns:
            plt.figure(figsize=(10, 4))
            plt.plot(sub['Data'], sub['max_heartrate'], color='darkred', marker='o')
            plt.title(f"{nome}: Heart Rate Máximo (BPM)")
            plt.grid(True, alpha=0.3); plt.show()

# Correr a análise
analise_claudia_2025()
