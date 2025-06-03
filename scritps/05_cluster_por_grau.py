# scripts/05_cluster_por_grau.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar base
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis para clustering
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

# 3. Reaplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 4. Recuperar a coluna "grau" da base original
df_completo = df.loc[df_cluster.index].copy()
df_completo['cluster'] = df_cluster['cluster']

# 5. Tabela cruzada: contagem de clusters por grau jurisdicional
tabela = pd.crosstab(df_completo['grau'], df_completo['cluster'])

# 6. Plotar gráfico
tabela.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title("Distribuição dos Clusters por Grau Jurisdicional")
plt.xlabel("Grau")
plt.ylabel("Quantidade de Órgãos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "clusters_por_grau.png"))
plt.show()

# 7. Mostrar a tabela no console
print("\nTabela de distribuição por grau:")
print(tabela)
