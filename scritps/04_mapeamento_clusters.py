# scripts/04_mapeamento_clusters.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar dados originais e limpos
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar colunas numéricas para clustering (as mesmas usadas antes)
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

# 3. Reaplicar KMeans (mesmo número de clusters = 3)
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 4. Reanexar rótulos ao DataFrame original (alinhando os índices)
df_cluster_completo = df.loc[df_cluster.index].copy()
df_cluster_completo['cluster'] = df_cluster['cluster']

# 5. Contagem de clusters por município
municipios_cluster = df_cluster_completo.groupby(['municipio', 'cluster']).size().unstack(fill_value=0)

# 6. Gráfico de barras empilhado por município
top_municipios = municipios_cluster.sum(axis=1).sort_values(ascending=False).head(15).index
municipios_cluster.loc[top_municipios].plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2')

plt.title("Distribuição dos Clusters por Município (Top 15)")
plt.xlabel("Município")
plt.ylabel("Quantidade de Órgãos")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "clusters_por_municipio.png"))
plt.show()

