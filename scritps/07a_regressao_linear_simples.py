# scripts/07a_regressao_linear_simples.py

import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar base com clusters
df = pd.read_csv(os.path.join("..", "dados", "TJSP_com_clusters.csv"))

# 2. Remover valores ausentes nas colunas selecionadas
df_modelo = df[['conc100_apr_2025', 'iad_12_meses']].dropna()

# 3. Definir variável dependente e independente
X = df_modelo[['conc100_apr_2025']]
y = df_modelo['iad_12_meses']

# 4. Ajustar modelo de regressão linear simples
modelo = LinearRegression()
modelo.fit(X, y)

# 5. Predições
y_pred = modelo.predict(X)

# 6. Avaliação do modelo
r2 = r2_score(y, y_pred)
rmse = mean_squared_error(y, y_pred) ** 0.5

print("Coeficiente angular (inclinação):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("R²:", round(r2, 4))
print("RMSE:", round(rmse, 2))

# 7. Visualização
plt.figure(figsize=(8, 5))
sns.regplot(x=X.values.flatten(), y=y, ci=None, scatter_kws={"alpha":0.5})
plt.title("Regressão Linear Simples: conc100_apr_2025 vs. IAD")
plt.xlabel("Conciliações Homologadas por 100 processos (conc100_apr_2025)")
plt.ylabel("Índice de Atendimento à Demanda (IAD)")
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "regressao_simples_iad.png"))
plt.show()