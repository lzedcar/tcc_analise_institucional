# scripts/07_modelo_preditivo.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Carregar base limpa
df = pd.read_csv(os.path.join("..", "dados", "TJSP_limpo_etapas.csv"))

# 2. Selecionar variáveis independentes e alvo (IAD)
variaveis = [
    'cp_apr_2025', 'sus_apr_2025', '%cp', '%sus',
    'desp_12_meses', 'sentcm_12_meses', 'tpsent_12_meses'
]

df_modelo = df[variaveis + ['iad_12_meses']].dropna()

X = df_modelo[variaveis]
y = df_modelo['iad_12_meses']

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar o modelo de regressão
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Avaliação
y_pred = modelo.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Modelo treinado com sucesso.")
print(f"Erro médio absoluto (MAE): {mae:.2f}")
print(f"R² (coeficiente de determinação): {r2:.3f}")

# 6. Coeficientes do modelo
print("\nCoeficientes:")
for var, coef in zip(variaveis, modelo.coef_):
    print(f"{var}: {coef:.2f}")

# 7. Gráfico: IAD real vs previsto
plt.figure()
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("IAD Real")
plt.ylabel("IAD Previsto")
plt.title("Modelo Preditivo - IAD (Real vs Previsto)")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.tight_layout()
plt.savefig(os.path.join("..", "graficos", "modelo_preditivo_iad.png"))
plt.show()

