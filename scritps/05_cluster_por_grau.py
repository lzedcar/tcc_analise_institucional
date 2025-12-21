# scripts/05_cluster_por_grau.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis relevantes com correlação confirmada
variaveis = ['tpsent_12_meses', 'tpcpl_apr_2025', 'conc100_apr_2025']
df_cluster = df[variaveis].dropna()

# 3. Padronizar os dados
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# 4. Aplicar KMeans com k=3 (mantendo consistência)
kmeans = KMeans(n_clusters=3, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(dados_padronizados)

# 5. Reanexar o grau jurisdicional da base original
df_completo = df.loc[df_cluster.index].copy()
df_completo['cluster'] = df_cluster['cluster']

# 6. Tabela cruzada: cluster x grau
tabela = pd.crosstab(df_completo['grau'], df_completo['cluster'])

# 7. Visualização
tabela.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title("Distribuição dos Clusters por Grau de Jurisdição")
plt.xlabel("Grau")
plt.ylabel("Quantidade de Órgãos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "clusters_por_grau.png"))
plt.show()

# 8. Mostrar no console
print("\nDistribuição dos clusters por grau:")
print(tabela)