import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CONFIGURAÇÃO FIXA
CLIENT_ID = '197799'
CLIENT_SECRET = '3019d7e204a6d8eef25460977f5a50e001b78503'
REFRESH_TOKEN = 'a0bff0bddada6d84eacc61310b13d93ba3895bd5'

def analise_eficiencia_claudia():
    # 1. Autenticação
    res = requests.post("https://www.strava.com/oauth/token", data={
        'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN, 'grant_type': 'refresh_token'
    }).json()
    token = res['access_token']
    
    headers = {'Authorization': f'Bearer {token}'}
    data = requests.get("https://www.strava.com/api/v3/athlete/activities", 
                        headers=headers, params={'per_page': 100}).json()
    
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['start_date_local'])
    df = df[df['Data'] >= '2025-01-01'].sort_values('Data')

    for tipo, nome_pt in [('Run', 'Corrida'), ('Swim', 'Natação')]:
        sub = df[df['type'] == tipo].copy()
        
        # Só calculamos se houver dados de Batimento Cardíaco
        if sub.empty or 'average_heartrate' not in sub.columns:
            continue
            
        sub = sub.dropna(subset=['average_heartrate'])

        # CÁLCULO DO ÍNDICE DE EFICIÊNCIA (Custo Cardíaco)
        # Na corrida: Batimentos por km
        # Na natação: Batimentos por 100m
        if tipo == 'Run':
            # (Tempo total em min * BPM médio) / Distância total em km
            sub['Eficiencia'] = (sub['moving_time'] / 60 * sub['average_heartrate']) / (sub['distance'] / 1000)
            label_y = "Batimentos por cada 1km"
        elif tipo == 'Swim':
            sub['Eficiencia'] = (sub['moving_time'] / 60 * sub['average_heartrate']) / (sub['distance'] / 100)
            label_y = "Batimentos por cada 100m"

        # --- GERAR GRÁFICO ---
        plt.figure(figsize=(12, 5))
        
        # Pontos reais de eficiência
        plt.plot(sub['Data'], sub['Eficiencia'], 'go', alpha=0.6, label='Índice por Treino')
        
        # Linha de Tendência de Eficiência
        if len(sub) > 1:
            x_idx = np.arange(len(sub))
            z = np.polyfit(x_idx, sub['Eficiencia'], 1)
            p = np.poly1d(z)
            plt.plot(sub['Data'], p(x_idx), "r--", label='Tendência de Eficiência')

        plt.title(f"EFICIÊNCIA EM 2025: {nome_pt.upper()}", fontweight='bold')
        plt.ylabel(label_y)
        plt.legend()
        plt.grid(True, alpha=0.2)
        
        # IMPORTANTE: Aqui quanto mais baixo o gráfico estiver, melhor! 
        # Significa que gastas menos "pulsações" para fazer a mesma distância.
        plt.show()

        print(f"Nota: No gráfico de {nome_pt}, a descida da linha indica que o teu coração está a tornar-se mais eficiente.")

analise_eficiencia_claudia()
