# scripts/02b_analise_correlacao.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Carregar a base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# Variáveis selecionadas para análise de correlação
variaveis = [
    "cp_apr_2025",
    "sus_apr_2025",
    "tpsent_12_meses",
    "tpcpl_apr_2025",
    "iad_12_meses"
]

df_corr = df[variaveis].copy()

# Verificar valores ausentes
print("Valores ausentes nas variáveis selecionadas:")
print(df_corr.isnull().sum())

# Remover linhas com NA apenas para a análise de correlação
df_corr = df_corr.dropna()

# Cálculo da matriz de correlação
corr = df_corr.corr()

print("\nMatriz de Correlação:")
print(corr)

# Plot do heatmap com escala padronizada (-1 a +1)
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    vmin=-1,
    vmax=1,
    cmap="coolwarm",
    center=0,
    annot=True,
    fmt=".2f"
)

plt.tight_layout()

# Salvar figura
plt.savefig(
    os.path.join("..", "graficos", "02b_correlacao_variaveis.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()