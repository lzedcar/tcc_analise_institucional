# scripts/02b_analise_correlacao.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Carregar a base limpa com o mesmo padrão de caminho dos scripts anteriores
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# Selecionar apenas colunas numéricas relevantes para correlação
variaveis_interesse = ['cp_apr_2025', 'sus_apr_2025', 'tpsent_12_meses', 
                       'tpcpl_apr_2025', 'iad_12_meses']

df_corr = df[variaveis_interesse].copy()

# Verificar e exibir valores ausentes
print("Valores ausentes nas variáveis selecionadas:")
print(df_corr.isnull().sum())

# Eliminar linhas com dados ausentes apenas para fins de correlação
df_corr = df_corr.dropna()

# Matriz de correlação
correlacao = df_corr.corr()

print("\nMatriz de Correlação:")
print(correlacao)

# Visualizar a matriz de correlação com heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação – Variáveis Operacionais")
plt.tight_layout()

# Salvar o gráfico
plt.savefig(os.path.join("..", "graficos", "02b_correlacao_variaveis.png"))
plt.show()
