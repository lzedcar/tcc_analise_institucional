# scripts/00_etapas_limpeza_manual.py

# ----------------------------------------
# Etapa 1 – Carregar e inspecionar os dados
# ----------------------------------------
import pandas as pd

# Lendo o arquivo bruto (formato original)
df = pd.read_csv("../dados/TJSP_tbl_correg.csv", sep=";", encoding="utf-8")

# Verificando estrutura
print("Informações iniciais da base:")
print(df.info())
print("\nPrimeiras linhas:")
print(df.head())

# ----------------------------------------
# Etapa 2 – Padronização dos nomes das colunas
# ----------------------------------------
# Justificativa: facilitar uso nos comandos, padronizar formato
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ----------------------------------------
# Etapa 3 – Análise de colunas com símbolos como "%"
# ----------------------------------------
# Exemplo: coluna '%cp' aparece como texto com símbolo
print("\nExemplo de valores em '%cp':")
print(df['%cp'].dropna().unique()[:10])

# Remover % e converter para float
df['%cp'] = df['%cp'].str.replace('%', '', regex=False).str.replace(',', '.')
df['%cp'] = pd.to_numeric(df['%cp'], errors='coerce')

# Repetir para outras colunas semelhantes
colunas_percentuais = ['%sus', 'tc_apr_2025', 'iad_12_meses']
for col in colunas_percentuais:
    df[col] = df[col].str.replace('%', '', regex=False).str.replace(',', '.')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ----------------------------------------
# Etapa 4 – Conversão de colunas de tempo (anos e meses → meses totais)
# ----------------------------------------
import re
import numpy as np

def tempo_para_meses(texto):
    if pd.isna(texto):
        return np.nan
    texto = texto.lower()
    anos = int(re.search(r'(\d+)\s+anos?', texto).group(1)) if re.search(r'(\d+)\s+anos?', texto) else 0
    meses = int(re.search(r'(\d+)\s+meses?', texto).group(1)) if re.search(r'(\d+)\s+meses?', texto) else 0
    return anos * 12 + meses

# Aplicar a conversão
df['tpsent_12_meses'] = df['tpsent_12_meses'].apply(tempo_para_meses)
df['tpcpl_apr_2025'] = df['tpcpl_apr_2025'].apply(tempo_para_meses)

# ----------------------------------------
# Etapa 5 – Verificação final e exportação
# ----------------------------------------
print("\nResumo após limpeza:")
print(df.info())

# Salvar versão tratada (opcional nesta etapa)
df.to_csv("../dados/TJSP_limpo_etapas.csv", index=False)

