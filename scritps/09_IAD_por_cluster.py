import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho correto do arquivo
df = pd.read_csv(r'C:/Users/Windows/Arquivos de sistema/Desktop/tcc_analise_institucional/tcc_analise_institucional/dados/TJSP_com_clusters.csv')

# Verificar colunas
print(df.columns)

# Garantir que as colunas necessárias existem
assert 'cluster' in df.columns, "Coluna 'cluster' não encontrada!"
assert 'iad_12_meses' in df.columns, "Coluna 'iad_12_meses' não encontrada!"

# 1. Estatística descritiva do IAD por cluster
iad_stats = df.groupby('cluster')['iad_12_meses'].describe()
print("\n📊 Estatísticas do IAD por cluster:\n")
print(iad_stats)

# 2. Boxplot
plt.figure(figsize=(10,6))
sns.boxplot(x='cluster', y='iad_12_meses', data=df, palette='Set2')
plt.title("Distribuição do IAD por Cluster")
plt.xlabel("Cluster")
plt.ylabel("IAD (12 meses)")
plt.show()

# 3. Média do IAD por cluster
print("\n📌 Média do IAD por cluster:")
print(df.groupby('cluster')['iad_12_meses'].mean())
