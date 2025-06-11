# scripts/06_exportar_com_clusters.py

import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar base limpa e tratada
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar apenas variáveis com maior correlação com IAD
variaveis = ['tpsent_12_meses', 'tpcpl_apr_2025', 'conc100_apr_2025']
df_cluster = df[variaveis].dropna()

# 3. Padronizar os dados
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# 4. Aplicar KMeans com k=3
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 5. Anexar cluster à base original (com alinhamento de índices)
df_final = df.loc[df_cluster.index].copy()
df_final['cluster'] = df_cluster['cluster']

# 6. Exportar base enriquecida
df_final.to_csv(os.path.join("..", "dados", "TJSP_com_clusters.csv"), index=False)

print("Base exportada com sucesso para 'dados/TJSP_com_clusters.csv'")