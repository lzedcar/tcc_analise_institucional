# Diagnóstico de Desempenho Institucional no TJSP com Ciência de Dados  
Análise de padrões operacionais, desigualdade estrutural e gargalos a partir de dados públicos

## Descrição

Este repositório reúne os scripts, dados e visualizações desenvolvidos para o Trabalho de Conclusão de Curso MBA em Ciência e Análise de Dados – USP/Esalq (2025).

O objetivo da pesquisa foi aplicar técnicas de ciência de dados para investigar o desempenho institucional das unidades judiciais do Tribunal de Justiça de São Paulo (TJSP), com base em dados operacionais agregados e públicos, referentes ao período de maio de 2023 a abril de 2024, disponibilizados pelo Conselho Nacional de Justiça (CNJ). Foram identificados padrões de funcionamento, perfis institucionais recorrentes e unidades com desempenho atípico, contribuindo para o diagnóstico exploratório da heterogeneidade institucional no TJSP.

## Estrutura do repositório

tcc_analise_institucional/
├── dados/
│ ├── outliers_regressao_multipla.csv
│ ├── outliers_simples.csv
│ ├── TJSP_com_clusters.csv
│ └── TJSP_limpo.csv
│ └── TJSP_limpo_etapas.csv
│ └── TJSP_tbl_correg.csv
├── scripts/
│ ├── 00_etapas_limpeza_manual.py
│ ├── 01_carregar_limpar_dados.py
│ ├── 02_analise_exploratoria.py
│ ├── 02b_correlacao_variaveis.py
│ ├── 03_clustering.py
│ ├── 04_mapeamento_clusters.py
│ ├── 05_cluster_por_grau.py
│ ├── 06_exportar_com_clusters.py
│ └── 07_modelo_preditivo.py
│ └── 07a_regressao_linear_simples.py
│ └── 08_outliers_multipla.py
│ └── 08a_outliers_simples.py
├── graficos/
│ ├── clusters_pca.png
│ ├── cotovelo.png
│ ├── distribuicao_clusters_municipio.png
│ ├── distribuição_iad.png
│ ├── matriz_correlacao_indicadores.png
│ ├── matriz_correlacao_operacionais.png
│ ├── medias_indicadores.png
│ ├── outliers_regressao_multipla.png
│ ├── outliers_regressao_simples.png
│ ├── regressao_multipla.png
│ └── regressao_simples.png

## Tecnologias utilizadas

- Python 3.12  
- Spyder 5.5.1  
- Pandas — manipulação de dados  
- NumPy — operações numéricas  
- Matplotlib e Seaborn — visualizações  
- Scikit-learn — clustering, regressão e padronização  
- OS e Pathlib — estruturação de scripts e diretórios  

## Metodologia aplicada

- Padronização e limpeza da base de dados (.csv)  
- Análise exploratória descritiva  
- Avaliação de correlação entre variáveis e o Índice de Atendimento à Demanda (IAD)  
- Agrupamento de unidades com K-Means (K=3)  
- Análise de distribuição dos clusters por município e grau  
- Regressão linear (simples e múltipla) como recurso exploratório  
- Identificação de outliers a partir dos resíduos dos modelos  
- Exportação da base final com clusterização aplicada  

## Principais descobertas

- Três perfis operacionais distintos identificados (baixo desempenho, intermediário e alto desempenho)  
- Unidades do primeiro grau concentram os piores desempenhos institucionais  
- A modelagem preditiva apresentou explicabilidade muito baixa (R² ≈ 0,0002 a -0,17)  
- A análise de outliers destacou unidades com desempenho atípico, que podem indicar gargalos ou boas práticas  
- O grau de jurisdição mostrou associação com o desempenho médio dos clusters  
- A análise quantitativa agregada é útil, mas limitada para explicar variações de desempenho institucional  

## Limitações

- Base exclusivamente agregada e quantitativa, sem variáveis qualitativas ou contextuais  
- Ausência de classificação confiável por tipo de vara impossibilitou estratificação por especialização  
- Regressões tiveram uso exclusivamente exploratório, sem finalidade preditiva  
- Comparações entre tipos de órgãos foram feitas com cautela metodológica devido à heterogeneidade funcional  

## Referências

- Conselho Nacional de Justiça [CNJ]. Justiça em Números – Painel de Estatísticas. Brasília, DF, Brasil. Disponível em: <https://justica-em-numeros.cnj.jus.br/painel-estatisticas/>. Acesso em: 03 de junho de 2025.
- Cunha, M. A.; Miranda, R. M. (2013). O uso de tecnologias de informação no Judiciário brasileiro: oportunidades e desafios. *Revista de Administração Pública*, 47(6): 1473–1493. <https://doi.org/10.1590/S0034-76122013000600006>
- Da Ros, Luciano. 2015. O custo da Justiça no Brasil: uma análise comparativa exploratória. Newsletter. Observatório de elites políticas e sociais do Brasil. NUSP/UFPR, v.2, n. 9, julho. p. 1-15. ISSN 2359-2826. < http://observatory-elites.org/wp-content/uploads/2012/06/newsletter-Observatorio-v.-2-n.-9.pdf>
- Domingos, P. 2015. The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World. New York, NY, USA: Basic Books.
- Favero, L. P.; Belfiore, P. 2017. Manual de Análise de Dados: Estatística e Modelagem Multivariada com Excel, SPSS e Stata. São Paulo, SP, Brasil: Elsevier. 660 p.
- Hastie, T.; Tibshirani, R.; Friedman, J. 2009. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2. ed. New York, NY, USA: Springer. 745 p.
- Pedregosa, F. et al. 2011. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12: 2825–2830.< http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>
- Porto, A. C. 2019. O impacto da transformação digital no judiciário brasileiro: uma análise da adoção de tecnologias no sistema judicial. Revista Eletrônica do TRT da 9ª Região, 9(96): 1–17.
- Ribeiro, M. V. M. (2024). A importância da inteligência artificial no poder judiciário brasileiro. REVISTA DELOS, 17(61), e2804. <https://doi.org/10.55905/rdelosv17.n61-142>. Acessado em: 15 de março de 2025.
- Russell, S.; Norvig, P. 2021. Artificial Intelligence: A Modern Approach. 4. ed. Upper Saddle River, NJ, USA: Pearson.
- Silva, G. C.; Macedo, T. S. 2020. Aplicações de ciência de dados no setor público: um estudo de caso no Poder Judiciário. Revista de Administração Pública e Gestão Social, 12(3): 229–245. https://doi.org/10.21118/apgs.v12i3.8204
- TRIBUNAL DE JUSTIÇA DO ESTADO DE SÃO PAULO. Órgãos da Justiça. Disponível em: https://www.tjsp.jus.br/PoderJudiciario/PoderJudiciario/OrgaosDaJustica. Acesso em: 11 jun. 2025.

## Autoria

Este repositório foi desenvolvido por Luciana Zedan de Carvalho como parte do Trabalho de Conclusão do Curso MBA em Data Science e Analytics USP/Esalq, 2025.
