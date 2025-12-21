import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Carregar a base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# Selecionar apenas variáveis numéricas
df_num = df.select_dtypes(include=["float64", "int64"])

print("Variáveis numéricas incluídas na matriz completa:")
print(df_num.columns.tolist())

# Remover linhas com NA apenas para correlação
df_num = df_num.dropna()

# Calcular matriz de correlação
corr_completa = df_num.corr()

print("\nMatriz de correlação completa:")
print(corr_completa)

# Plot do heatmap
plt.figure(figsize=(14, 12))
sns.heatmap(
    corr_completa,
    vmin=-1,
    vmax=1,
    center=0,
    cmap="coolwarm",
    annot=False  # importante: sem números para não poluir
)

plt.tight_layout()

# Salvar figura
plt.savefig(
    os.path.join("..", "graficos", "02a_correlacao_completa.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()

sns.heatmap(
    corr_completa,
    vmin=-1,
    vmax=1,
    center=0,
    cmap="coolwarm",
    annot=True,
    fmt=".2f",
    annot_kws={"size": 7}
)