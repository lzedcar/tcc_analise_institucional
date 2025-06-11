# scripts/08b_outliers_multipla.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carregar base de dados limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# Selecionar variáveis independentes e dependente
variaveis = ['tpsent_12_meses', 'tpcpl_apr_2025', 'conc100_apr_2025']
df_modelo = df[variaveis + ['iad_12_meses']].dropna()

X = df_modelo[variaveis]
y = df_modelo['iad_12_meses']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Prever valores
y_pred = modelo.predict(X_test)

# Calcular resíduos
residuos = y_test - y_pred
residuos_padronizados = (residuos - residuos.mean()) / residuos.std()

# Identificar outliers (resíduos padronizados > 3 ou < -3)
outliers = residuos[abs(residuos_padronizados) > 3]

# Mostrar no terminal
print("Unidades com resíduos atípicos (outliers):")
df_outliers = df.loc[outliers.index].copy()
df_outliers["iad_previsto"] = y_pred[[i for i, idx in enumerate(y_test.index) if idx in outliers.index]]
df_outliers["residuo"] = residuos[outliers.index]
print(df_outliers[[*variaveis, 'iad_12_meses', 'iad_previsto', 'residuo']])

# Gráfico com destaque para outliers
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, label="Dados")
plt.scatter(
    y_test.loc[outliers.index],
    y_pred[[i for i, idx in enumerate(y_test.index) if idx in outliers.index]],
    color='red', label="Outliers"
)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label="Referência")
plt.xlabel("IAD Real")
plt.ylabel("IAD Previsto")
plt.title("Outliers na Regressão Linear Múltipla")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "outliers_multipla.png"))
plt.show()

# Exportar CSV (opcional)
df_outliers.to_csv(os.path.join("..", "dados", "outliers_regressao_multipla.csv"), index=False)