import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base (ajuste o caminho se necessário)
df = pd.read_csv('/mnt/data/TJSP_com_clusters.csv')

# Identificar nome correto da coluna de cluster
cluster_col = None
for col in ['cluster', 'Cluster', 'cluster_id', 'Cluster_id']:
    if col in df.columns:
        cluster_col = col
        break

if cluster_col is None:
    raise ValueError("Nenhuma coluna de cluster encontrada na base!")

print("Coluna de cluster encontrada:", cluster_col)

# Verificar tipo da coluna do IAD
print("\nTipo da coluna IAD_12_meses:", df['IAD_12_meses'].dtype)

# Caso o IAD tenha porcentagens como texto, vamos limpar
if df['IAD_12_meses'].dtype == 'object':
    df['IAD_12_meses'] = (
        df['IAD_12_meses']
        .astype(str)
        .str.replace('%', '', regex=False)
        .str.replace(',', '.', regex=False)
    )
    df['IAD_12_meses'] = pd.to_numeric(df['IAD_12_meses'], errors='coerce')

# Remover registros sem IAD
df = df.dropna(subset=['IAD_12_meses'])

# Criar tabela de médias
iad_por_cluster = df.groupby(cluster_col)['IAD_12_meses'].agg(['mean', 'median', 'std', 'count'])
print("\nIAD por cluster:\n", iad_por_cluster)

# -----------------------------
# GRÁFICOS
# -----------------------------

# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x=cluster_col, y='IAD_12_meses')
plt.title("Distribuição do IAD por Cluster")
plt.xlabel("Cluster")
plt.ylabel("IAD (12 meses)")
plt.tight_layout()
plt.show()

# Violinplot (opcional)
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x=cluster_col, y='IAD_12_meses', inner="quartile")
plt.title("Distribuição do IAD por Cluster (Violinplot)")
plt.xlabel("Cluster")
plt.ylabel("IAD (12 meses)")
plt.tight_layout()
plt.show()
