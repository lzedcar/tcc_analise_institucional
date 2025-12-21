# Perfis operacionais e disparidades de desempenho entre unidades judiciárias do Tribunal de Justiça de São Paulo

**Análise de padrões operacionais, desigualdade estrutural e gargalos a partir de dados públicos**

## Descrição

Este repositório reúne os scripts, dados e visualizações desenvolvidos para o Trabalho de Conclusão de Curso (MBA em Ciência e Análise de Dados – USP/Esalq, 2025).

O objetivo da pesquisa foi aplicar técnicas de ciência de dados para investigar o desempenho institucional das unidades judiciais do Tribunal de Justiça de São Paulo (TJSP), com base em dados operacionais agregados e públicos, referentes ao período de **maio/2023 a abril/2024**, disponibilizados pelo **Conselho Nacional de Justiça (CNJ)**. Foram identificados padrões de funcionamento e perfis operacionais recorrentes, contribuindo para um diagnóstico exploratório da heterogeneidade institucional no TJSP.

## Estrutura do repositório

```text
tcc_analise_institucional/
│
├── dados/
│   ├── tabela_descritivas_eda.csv
│   ├── cargas_fatoriais_pca.csv
│   ├── cargas_pca.csv
│   ├── TJSP_com_clusters.csv
│   ├── TJSP_limpo.csv
│   ├── TJSP_limpo_etapas.csv
│   ├── TJSP_limpo_etapas_com_cluster_iad.csv
│   └── TJSP_tbl_correg.csv
│
├── scripts/
│   ├── 00_etapas_limpeza_manual.py
│   ├── 01_carregar_limpar_dados.py
│   ├── 01a_distribuicoes.py
│   ├── 02_analise_exploratoria.py
│   ├── 02b_correlacao_variaveis.py
│   ├── 02c_correlacao_variaveis.py
│   ├── 03_clustering.py
│   ├── 04_mapeamento_clusters.py
│   ├── 05_cluster_por_grau.py
│   ├── 06_exportar_com_clusters.py
│   ├── 08_IAD_por_clusterx.py
│   ├── 09_IAD_por_cluster.py
│   └── 10_graficotribunais.py
│
├── graficos/
│   ├── eda_boxplot_variaveis.png
│   ├── eda_hist_conc100_apr_2025.png
│   ├── eda_hist_tpcpl_apr_2025.png
│   ├── eda_hist_tpsent_12_meses.png
│   ├── eda_hist_iad_12_meses.png
│   ├── tabela_tipologia_tjsp.png
│   ├── 03_cargas_fatoriais_pca.png
│   ├── 03_medias_por_cluster.png
│   ├── 03_clusters_pca.png
│   ├── 03_cotovelo_kmeans.png
│   ├── correlacao_completa.png
│   ├── 02a_correlacao_completa_cores.png
│   ├── matriz_reduzida.png
│   ├── distribuicao_iad.png
│   ├── distribuicao_IAD_por_cluster.png
│   ├── clusters_por_grau.png
│   └── distribuicao_clusters_municipio.png
│
└── README.md
```

## Tecnologias utilizadas

* Python 3.12
* Spyder 5.5.1
* Pandas (manipulação de dados)
* NumPy (operações numéricas)
* Matplotlib e Seaborn (visualizações)
* Scikit-learn (padronização, K-Means e PCA)
* OS e Pathlib (estruturação de scripts e diretórios)

## Metodologia aplicada (visão geral)

* Padronização e limpeza da base de dados (.csv)
* Análise exploratória descritiva
* Avaliação de correlação entre variáveis e o Índice de Atendimento à Demanda (IAD)
* Agrupamento de unidades com K-Means (k = 3)
* PCA como apoio exploratório e visual
* Análise de distribuição dos clusters por município e grau
* Exportação da base final com clusterização aplicada

## Principais descobertas

* Identificação de **três perfis operacionais** distintos (clusters) com padrões diferentes de tempo e conciliação.
* Maior concentração de unidades do **1º grau** nos perfis de menor desempenho.
* Evidências de **heterogeneidade institucional** relevante entre unidades do mesmo tribunal.
* Utilidade de métodos exploratórios e não supervisionados para **diagnóstico institucional** a partir de dados públicos agregados.

## Limitações

* Base exclusivamente agregada e quantitativa, sem variáveis qualitativas ou contextuais.
* Ausência de classificação confiável por tipo de vara, dificultando estratificação por especialização.
* Comparações entre tipos de órgãos exigem cautela metodológica devido à heterogeneidade funcional.

## Referências

* Conselho Nacional de Justiça (CNJ). *Justiça em Números – Painel de Estatísticas*. Acesso em: 03 jun. 2025.
* Cunha, M. A.; Miranda, R. M. (2013). O uso de tecnologias de informação no Judiciário brasileiro: oportunidades e desafios. *Revista de Administração Pública*, 47(6), 1473–1493.
* Da Ros, L. (2015). O custo da Justiça no Brasil: uma análise comparativa exploratória.
* Hastie, T.; Tibshirani, R.; Friedman, J. (2009). *The Elements of Statistical Learning*. 2nd ed. Springer.
* Pedregosa, F. et al. (2011). Scikit-learn: Machine learning in Python. *JMLR*, 12, 2825–2830.
* Porto, A. C. (2019). O impacto da transformação digital no judiciário brasileiro.
* Ribeiro, M. V. M. (2024). A importância da inteligência artificial no poder judiciário brasileiro. *REVISTA DELOS*, 17(61).
* Silva, G. C.; Macedo, T. S. (2020). Aplicações de ciência de dados no setor público: um estudo de caso no Poder Judiciário.
* TJSP. *Órgãos da Justiça*. Acesso em: 11 jun. 2025.

## Autoria

Este repositório foi desenvolvido por **Luciana Zedan de Carvalho** como parte do Trabalho de Conclusão do Curso (MBA em Data Science e Analytics – USP/Esalq, 2025).
