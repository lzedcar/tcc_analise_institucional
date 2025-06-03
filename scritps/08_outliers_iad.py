# scripts/08_outliers_iad.py

import pandas as pd
import os

# 1. Carregar a base final com clusters
df = pd.read_csv(os.path.join("..", "dados", "TJSP_com_clusters.csv"))

# 2. Remover casos sem IAD
df = df.dropna(subset=['iad_12_meses'])

# 3. Ordenar por IAD (crescente e decrescente)
menores_iad = df.sort_values('iad_12_meses').head(5)
maiores_iad = df.sort_values('iad_12_meses', ascending=False).head(5)

# 4. Selecionar colunas relevantes para análise
colunas = [
    'codigo_orgao', 'nome_orgao', 'municipio', 'grau',
    'iad_12_meses', 'cp_apr_2025', 'desp_12_meses', 
    'tpsent_12_meses', 'cluster'
]

print("\n🔴 Órgãos com os MENORES IADs (potenciais gargalos):")
print(menores_iad[colunas])

print("\n🟢 Órgãos com os MAIORES IADs (fora da curva ou exceções):")
print(maiores_iad[colunas])

import matplotlib.pyplot as plt

# 5. Gerar gráfico de distribuição com destaque para outliers
plt.figure(figsize=(10, 6))
plt.hist(df['iad_12_meses'], bins=30, alpha=0.6, edgecolor='black', label='Todos os órgãos')

# Marcar os outliers com linhas verticais
for x in menores_iad['iad_12_meses']:
    plt.axvline(x, color='red', linestyle='--', linewidth=1.5, label='Menor IAD' if x == menores_iad['iad_12_meses'].iloc[0] else "")

for x in maiores_iad['iad_12_meses']:
    plt.axvline(x, color='green', linestyle='--', linewidth=1.5, label='Maior IAD' if x == maiores_iad['iad_12_meses'].iloc[0] else "")

plt.title('Distribuição do Índice de Atendimento à Demanda (IAD)')
plt.xlabel('IAD (12 meses)')
plt.ylabel('Número de Órgãos')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()