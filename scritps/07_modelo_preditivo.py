# scripts/07_modelo_preditivo.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis com maior correlação com o IAD
variaveis_independentes = ['tpsent_12_meses', 'tpcpl_apr_2025', 'conc100_apr_2025']
variavel_dependente = 'iad_12_meses'

df_modelo = df[variaveis_independentes + [variavel_dependente]].dropna()

X = df_modelo[variaveis_independentes]
y = df_modelo[variavel_dependente]

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Avaliar modelo
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # <-- correção aqui
r2 = r2_score(y_test, y_pred)

print("Modelo treinado com sucesso.")
print(f"Erro médio absoluto (MAE): {mae:.2f}")
print(f"Raiz do erro quadrático médio (RMSE): {rmse:.2f}")
print(f"R² (coeficiente de determinação): {r2:.3f}")

# 6. Coeficientes
print("\nCoeficientes do modelo:")
for var, coef in zip(variaveis_independentes, modelo.coef_):
    print(f"{var}: {coef:.4f}")
print(f"Intercepto: {modelo.intercept_:.4f}")

# 7. Gráfico: valores reais vs previstos
plt.figure()
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("IAD Real")
plt.ylabel("IAD Previsto")
plt.title("Regressão Linear Múltipla – IAD Real vs Previsto")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "modelo_preditivo_iad.png"))
plt.show()