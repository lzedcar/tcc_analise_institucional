# scripts/03_clustering.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os

# Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# ----------------------------------------
# Seleção de variáveis com base na análise de correlação
# ----------------------------------------
# Foco em variáveis com maior associação com o desempenho (IAD)
# Evita inclusão de variáveis com correlação fraca ou irrelevante
variaveis = [
    'tpsent_12_meses',    # Tempo médio de sentença
    'tpcpl_apr_2025',     # Tempo médio de cumprimento
    'conc100_apr_2025'    # Taxa de conclusão
]

df_cluster = df[variaveis].dropna()  # Remover linhas com valores ausentes

# Padronizar os dados
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# ----------------------------------------
# Etapa 1 – Método do cotovelo para definir número ideal de clusters
# ----------------------------------------
inercia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(dados_padronizados)
    inercia.append(kmeans.inertia_)

plt.figure()
plt.plot(k_range, inercia, marker='o')
plt.title("Método do Cotovelo para Escolher K")
plt.xlabel("Número de Clusters (k)")
plt.ylabel("Inércia (Soma das Distâncias)")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "cotovelo_kmeans.png"))
plt.show()

# ----------------------------------------
# Etapa 2 – Aplicar KMeans com número ideal de clusters
# ----------------------------------------
k_ideal = 3  # Pode ser ajustado após visualização

kmeans_final = KMeans(n_clusters=k_ideal, random_state=42)
df_cluster['cluster'] = kmeans_final.fit_predict(dados_padronizados)

# ----------------------------------------
# Etapa 3 – Visualização com PCA (redução de dimensão para 2D)
# ----------------------------------------
pca = PCA(n_components=2)
componentes = pca.fit_transform(dados_padronizados)

plt.figure()
sns.scatterplot(x=componentes[:, 0], y=componentes[:, 1], hue=df_cluster['cluster'], palette='Set2')
plt.title("Visualização dos Clusters (PCA)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "clusters_pca.png"))
plt.show()

# ----------------------------------------
# Etapa 4 – Perfil médio de cada grupo
# ----------------------------------------
print("\nPerfil médio por cluster:")
print(df_cluster.groupby('cluster').mean())

# ----------------------------------------
# Etapa 5 – Gráfico: Comparativo das médias por cluster
# ----------------------------------------
medias = df_cluster.groupby('cluster').mean()

plt.figure(figsize=(10, 5))
medias.T.plot(kind='bar')
plt.title("Médias de Indicadores Operacionais por Cluster")
plt.ylabel("Valor Médio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "medias_por_cluster.png"))
plt.show()