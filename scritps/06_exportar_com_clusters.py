# scripts/06_exportar_com_clusters.py

import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis numéricas (iguais às anteriores)
variaveis = [
    'cp_apr_2025', 'sus_apr_2025', '%cp', '%sus', 'cn_12_meses',
    'tbaix_12_meses', 'desp_12_meses', 'decinc_12_meses',
    'sentcm_12_meses', 'sentsm_12_meses', 'procsm100_apr_2025',
    'conc100_apr_2025', 'tc_apr_2025', 'iad_12_meses',
    'tpsent_12_meses', 'tpcpl_apr_2025'
]

df_cluster = df[variaveis].dropna()
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# 3. Reaplicar KMeans com k=3
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 4. Reunir a base final com os dados originais + cluster
df_final = df.loc[df_cluster.index].copy()
df_final['cluster'] = df_cluster['cluster']

# 5. Exportar
df_final.to_csv(os.path.join("..", "dados", "TJSP_com_clusters.csv"), index=False)

print("✅ Base exportada com sucesso para 'dados/TJSP_com_clusters.csv'")
