# scripts/08a_outliers_simples.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis relevantes
df_modelo = df[['conc100_apr_2025', 'iad_12_meses']].dropna()

X = df_modelo[['conc100_apr_2025']]
y = df_modelo['iad_12_meses']

# 3. Treinar regressão simples
modelo = LinearRegression()
modelo.fit(X, y)

# 4. Previsão e cálculo dos resíduos
df_modelo['previsto'] = modelo.predict(X)
df_modelo['residuo'] = df_modelo['iad_12_meses'] - df_modelo['previsto']

# 5. Identificar outliers (resíduos fora de 2 desvios padrão)
limite_superior = df_modelo['residuo'].mean() + 2 * df_modelo['residuo'].std()
limite_inferior = df_modelo['residuo'].mean() - 2 * df_modelo['residuo'].std()

outliers = df_modelo[(df_modelo['residuo'] > limite_superior) | (df_modelo['residuo'] < limite_inferior)]

# 6. Exibir e salvar outliers
print("\nUnidades com resíduos atípicos (outliers):")
print(outliers[['conc100_apr_2025', 'iad_12_meses', 'previsto', 'residuo']])

outliers.to_csv(os.path.join("..", "dados", "outliers_simples.csv"), index=False)

# 7. Visualização
plt.figure(figsize=(10, 6))
plt.scatter(df_modelo['conc100_apr_2025'], df_modelo['iad_12_meses'], alpha=0.4, label="Dados")
plt.scatter(outliers['conc100_apr_2025'], outliers['iad_12_meses'], color='red', label="Outliers")
plt.plot(X, df_modelo['previsto'], color='green', linewidth=2, label="Regressão Linear")
plt.xlabel("Conciliações por 100 processos (conc100_apr_2025)")
plt.ylabel("Índice de Atendimento à Demanda (IAD)")
plt.title("Outliers na Regressão Linear Simples")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "outliers_simples.png"))
plt.show()

