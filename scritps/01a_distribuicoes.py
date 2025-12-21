# =========================================
# EDA – Distribuição das variáveis centrais
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------
# Carregamento da base (caminho absoluto)
# -----------------------------------------
df = pd.read_csv(
    r"C:\Users\Windows\Arquivos de sistema\Desktop\tcc_analise_institucional\tcc_analise_institucional\dados\TJSP_limpo_etapas.csv"
)

# -----------------------------------------
# Variáveis analisadas
# -----------------------------------------
variaveis_eda = [
    "iad_12_meses",
    "tpsent_12_meses",
    "tpcpl_apr_2025",
    "conc100_apr_2025"
]

# -----------------------------------------
# Estatísticas descritivas
# -----------------------------------------
descritivas = df[variaveis_eda].describe().T
print("\nEstatísticas descritivas das variáveis analisadas:")
print(descritivas)

# Salvar tabela de descritivas para uso no TCC
descritivas.to_csv(
    r"C:\Users\Windows\Arquivos de sistema\Desktop\tcc_analise_institucional\tcc_analise_institucional\dados\tabela_descritivas_eda.csv"
)

# -----------------------------------------
# Histogramas individuais
# -----------------------------------------
for var in variaveis_eda:
    serie = df[var].dropna()

    plt.figure(figsize=(7, 4))
    sns.histplot(
        serie,
        bins=30,
        kde=True,
        color="#4C72B0"
    )
    plt.xlabel(var)
    plt.ylabel("Frequência")
    plt.tight_layout()

    plt.savefig(
        fr"C:\Users\Windows\Arquivos de sistema\Desktop\tcc_analise_institucional\tcc_analise_institucional\graficos\eda_hist_{var}.png",
        dpi=300
    )
    plt.show()

# -----------------------------------------
# Boxplot conjunto (dispersão geral)
# -----------------------------------------
plt.figure(figsize=(8, 4))
sns.boxplot(
    data=df[variaveis_eda],
    orient="h",
    color="#DD8452"
)
plt.tight_layout()

plt.savefig(
    r"C:\Users\Windows\Arquivos de sistema\Desktop\tcc_analise_institucional\tcc_analise_institucional\graficos\eda_boxplot_variaveis.png",
    dpi=300
)
plt.show()