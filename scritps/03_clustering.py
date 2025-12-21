# scripts/03_clustering.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os

# --------------------------------------------------
# 1. Carregamento da base de dados
# --------------------------------------------------

df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# --------------------------------------------------
# 2. Seleção das variáveis operacionais
# --------------------------------------------------
# Variáveis selecionadas com base em critério teórico
# e análise exploratória de correlação

variaveis = [
    "tpsent_12_meses",     # Tempo médio para sentença
    "tpcpl_apr_2025",      # Tempo médio para conclusão
    "conc100_apr_2025"     # Conciliações por 100 processos
]

df_cluster = df[variaveis].dropna()

# --------------------------------------------------
# 3. Padronização das variáveis
# --------------------------------------------------

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df_cluster)

# --------------------------------------------------
# 4. Definição do número de clusters – Método do Cotovelo
# --------------------------------------------------

inercia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(dados_padronizados)
    inercia.append(kmeans.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(k_range, inercia, marker="o")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inércia")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "03_cotovelo_kmeans.png"))
plt.show()

# --------------------------------------------------
# 5. Aplicação do K-Means
# --------------------------------------------------

k_ideal = 3

kmeans_final = KMeans(n_clusters=k_ideal, random_state=42)
df_cluster["cluster"] = kmeans_final.fit_predict(dados_padronizados)

# --------------------------------------------------
# 6. Análise de Componentes Principais (PCA)
# --------------------------------------------------

pca = PCA(n_components=2)
componentes = pca.fit_transform(dados_padronizados)

# Variância explicada
variancia_explicada = pca.explained_variance_ratio_

print("\nVariância explicada por componente:")
for i, var in enumerate(variancia_explicada, start=1):
    print(f"PC{i}: {var:.2%}")

# Cargas fatoriais
loadings = pd.DataFrame(
    pca.components_.T,
    index=variaveis,
    columns=["PC1", "PC2"]
)

print("\nCargas fatoriais do PCA:")
print(loadings)

# Salvar tabela de cargas fatoriais
loadings.to_csv(os.path.join("..", "dados", "cargas_fatoriais_pca.csv"))

# --------------------------------------------------
# 7. Visualização dos clusters no espaço do PCA
# --------------------------------------------------

plt.figure(figsize=(7, 5))
sns.scatterplot(
    x=componentes[:, 0],
    y=componentes[:, 1],
    hue=df_cluster["cluster"],
    palette="Set2",
    s=40
)
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "03_clusters_pca.png"))
plt.show()

# --------------------------------------------------
# 8. Perfil médio dos clusters
# --------------------------------------------------

medias = df_cluster.groupby("cluster").mean()

print("\nPerfil médio por cluster:")
print(medias)

plt.figure(figsize=(8, 4))
medias.T.plot(kind="bar")
plt.ylabel("Valor médio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "03_medias_por_cluster.png"))
plt.show()

# --------------------------------------------------
# 9. Gráfico das cargas fatoriais
# --------------------------------------------------

plt.figure(figsize=(7, 4))
loadings.plot(kind="bar")
plt.axhline(0, color="black", linewidth=0.8)
plt.ylabel("Carga fatorial")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "03_cargas_fatoriais_pca.png"))
plt.show()
