# scripts/02_analise_exploratoria.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carregar a base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# ----------------------------------------
# Estatísticas descritivas
# ----------------------------------------
print("\nResumo estatístico das variáveis numéricas:")
print(df.describe())

# ----------------------------------------
# Valores ausentes
# ----------------------------------------
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# ----------------------------------------
# Distribuição do Índice de Atendimento à Demanda (IAD)
# ----------------------------------------
plt.figure()
sns.histplot(df['iad_12_meses'].dropna(), kde=True)
plt.title("Distribuição do IAD (Índice de Atendimento à Demanda)")
plt.xlabel("IAD")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "distribuicao_iad.png"))
plt.show()

# ----------------------------------------
# Matriz de correlação
# ----------------------------------------
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matriz de Correlação entre Indicadores")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "correlacao_indicadores.png"))
plt.show()


