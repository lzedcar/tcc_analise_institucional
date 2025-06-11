# scripts/04_mapeamento_clusters.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar a base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis com maior correlação com o IAD
variaveis = ['tpsent_12_meses', 'tpcpl_apr_2025', 'conc100_apr_2025']
df_cluster = df[variaveis].dropna()

# 3. Padronizar os dados
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# 4. Aplicar novamente o KMeans (mesmo número de clusters = 3)
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 5. Reanexar os rótulos ao DataFrame original (com alinhamento de índice)
df_cluster_completo = df.loc[df_cluster.index].copy()
df_cluster_completo['cluster'] = df_cluster['cluster']

# 6. Contar número de órgãos por cluster e município
municipios_cluster = df_cluster_completo.groupby(['municipio', 'cluster']).size().unstack(fill_value=0)

# 7. Gráfico de barras empilhado (Top 15 municípios)
top_municipios = municipios_cluster.sum(axis=1).sort_values(ascending=False).head(15).index
municipios_cluster.loc[top_municipios].plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2')

plt.title("Distribuição dos Clusters por Município (Top 15)")
plt.xlabel("Município")
plt.ylabel("Quantidade de Órgãos")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "clusters_por_municipio.png"))
plt.show()