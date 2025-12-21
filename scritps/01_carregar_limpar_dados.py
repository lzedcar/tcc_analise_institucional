# scripts/01_carregar_limpar_dados.py

import pandas as pd
import numpy as np
import os
import re

# Caminho do arquivo CSV
caminho_arquivo = os.path.join("..", "dados", "TJSP_tbl_correg.csv")

# Carregando os dados
df = pd.read_csv(caminho_arquivo, encoding='utf-8', sep=';')

# Padronizar nomes de colunas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Converter percentuais para float
def limpar_percentuais(col):
    df[col] = df[col].str.replace('%', '', regex=False)
    df[col] = df[col].str.replace(',', '.', regex=False)
    df[col] = df[col].apply(lambda x: re.sub(r'(?<=\d)\.(?=\d{3}\.)', '', x) if isinstance(x, str) else x)
    df[col] = pd.to_numeric(df[col], errors='coerce')

colunas_percentuais = ['%cp', '%sus', 'tc_apr_2025', 'iad_12_meses']
for col in colunas_percentuais:
    if col in df.columns:
        limpar_percentuais(col)

# Converter tempo (anos e meses) para meses inteiros
def tempo_para_meses(texto):
    if pd.isna(texto):
        return np.nan
    texto = texto.lower()
    anos = int(re.search(r'(\d+)\s+anos?', texto).group(1)) if re.search(r'(\d+)\s+anos?', texto) else 0
    meses = int(re.search(r'(\d+)\s+meses?', texto).group(1)) if re.search(r'(\d+)\s+meses?', texto) else 0
    return anos * 12 + meses

if 'tpsent_12_meses' in df.columns:
    df['tpsent_12_meses'] = df['tpsent_12_meses'].apply(tempo_para_meses)

if 'tpcpl_apr_2025' in df.columns:
    df['tpcpl_apr_2025'] = df['tpcpl_apr_2025'].apply(tempo_para_meses)

# Visualizar o resultado
print(df.info())
print(df.head())

# (Opcional) Salvar versão limpa
df.to_csv(os.path.join("..", "dados", "TJSP_limpo.csv"), index=False)

