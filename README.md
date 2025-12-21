# Perfis operacionais e disparidades de desempenho entre unidades judiciárias do Tribunal de Justiça de São Paulo

Análise de padrões operacionais, desigualdade estrutural e heterogeneidade institucional a partir de dados públicos

---

## Descrição

Este repositório reúne os scripts, bases de dados e visualizações desenvolvidos para o **Trabalho de Conclusão de Curso do MBA em Ciência e Análise de Dados – USP/ESALQ (2025)**.

O objetivo da pesquisa foi aplicar técnicas de ciência de dados, com enfoque **exploratório e diagnóstico**, para investigar o desempenho institucional das unidades judiciais do **Tribunal de Justiça de São Paulo (TJSP)**, a partir de **dados operacionais agregados e públicos**, referentes ao período de **maio de 2023 a abril de 2024**, disponibilizados pelo **Conselho Nacional de Justiça (CNJ)** no Painel *Justiça em Números*.

A análise buscou identificar padrões de funcionamento, perfis institucionais recorrentes e desigualdades estruturais entre os órgãos judiciais, contribuindo para o diagnóstico exploratório da heterogeneidade institucional no TJSP.

---

## Estrutura do repositório

tcc_analise_institucional/
│
├── dados/
│ ├── tabela_descritivas_eda.csv
│ ├── cargas_fatoriais_pca.csv
│ ├── cargas_pca.csv
│ ├── TJSP_limpo.csv
│ ├── TJSP_limpo_etapas.csv
│ ├── TJSP_com_clusters.csv
│ ├── TJSP_limpo_etapas_com_cluster_iad.csv
│ └── TJSP_tbl_correg.csv
│
├── scripts/
│ ├── 00_etapas_limpeza_manual.py
│ ├── 01_carregar_limpar_dados.py
│ ├── 01a_distribuicoes.py
│ ├── 02_analise_exploratoria.py
│ ├── 02b_correlacao_variaveis.py
│ ├── 02c_correlacao_variaveis.py
│ ├── 03_clustering.py
│ ├── 04_mapeamento_clusters.py
│ ├── 05_cluster_por_grau.py
│ ├── 06_exportar_com_clusters.py
│ ├── 08_IAD_por_clusterx.py
│ ├── 09_IAD_por_cluster.py
│ └── 10_graficotribunais.py
│
├── graficos/
│ ├── eda_boxplot_variaveis.png
│ ├── eda_hist_conc100_apr_2025.png
│ ├── eda_hist_tpcpl_apr_2025.png
│ ├── eda_hist_tpsent_12_meses.png
│ ├── eda_hist_iad_12_meses.png
│ ├── tabela_tipologia_tjsp.png
│ ├── 03_cargas_fatoriais_pca.png
│ ├── 03_medias_por_cluster.png
│ ├── 03_clusters_pca.png
│ ├── 03_cotovelo_kmeans.png
│ ├── correlacao_completa.png
│ ├── 02a_correlacao_completa_cores.png
│ ├── matriz_reduzida.png
│ ├── distribuicao_iad.png
│ ├── distribuicao_IAD_por_cluster.png
│ ├── clusters_por_grau.png
│ └── distribuicao_clusters_municipio.png
│
└── README.md

yaml
Copiar código

---

## Tecnologias utilizadas

- Python 3.12  
- Spyder 5.5.1  
- Pandas — manipulação e tratamento de dados  
- NumPy — operações numéricas  
- Matplotlib e Seaborn — visualizações  
- Scikit-learn — padronização, K-Means e PCA  
- OS e Pathlib — organização de diretórios e scripts  

---

## Metodologia aplicada

- Limpeza e padronização da base de dados do CNJ  
- Análise exploratória descritiva (EDA)  
- Avaliação de correlação entre indicadores operacionais e o Índice de Atendimento à Demanda (IAD), com finalidade exploratória  
- Seleção teórica e empírica das variáveis operacionais  
- Agrupamento não supervisionado com **K-Means (k = 3)**  
- Análise de Componentes Principais (PCA) para **validação visual e interpretação dos clusters**  
- Análise da distribuição dos clusters por grau de jurisdição e municípios  
- Avaliação descritiva do IAD a posteriori, sem uso como variável de segmentação  

---

## Principais achados

- Identificação de **três perfis operacionais distintos** entre as unidades judiciais do TJSP  
- Concentração de unidades com **menor desempenho operacional no primeiro grau de jurisdição**  
- O cluster com melhores indicadores apresentou maior presença relativa de **unidades com funções diferenciadas ou especializadas**  
- Baixa associação entre indicadores operacionais agregados e o **Índice de Atendimento à Demanda (IAD)**  
- Evidência de que o desempenho institucional **não pode ser explicado apenas por métricas quantitativas agregadas**  
- Indicação da influência de fatores estruturais, organizacionais e humanos não observáveis na base analisada  

---

## Limitações

- Base de dados agregada por unidade judicial, sem acesso a processos individuais  
- Ausência de variáveis qualitativas e contextuais (estrutura de pessoal, informatização, complexidade das causas)  
- Inexistência de classificação padronizada por tipo de vara ou especialização temática  
- Análises com caráter exploratório e descritivo, sem pretensão causal ou preditiva  
- Comparações realizadas com cautela devido à heterogeneidade funcional dos órgãos judiciais  

---

## Referências

Conselho Nacional de Justiça (CNJ). Justiça em Números – Painel de Estatísticas.  
Cunha, M. A.; Miranda, R. M. (2013).  
Da Ros, L. (2015).  
Domingos, P. (2015).  
Favero, L. P.; Belfiore, P. (2017).  
Hastie, T.; Tibshirani, R.; Friedman, J. (2009).  
Pedregosa, F. et al. (2011).  
Porto, A. C. (2019).  
Ribeiro, M. V. M. (2024).  
Russell, S.; Norvig, P. (2021).  
Silva, G. C.; Macedo, T. S. (2020).  
Tribunal de Justiça do Estado de São Paulo (TJSP). Órgãos da Justiça.

---

## Autoria

Este repositório foi desenvolvido por **Luciana Zedan de Carvalho**, como parte do **Trabalho de Conclusão do MBA em Ciência e Análise de Dados – USP/ESALQ (2025)**.
