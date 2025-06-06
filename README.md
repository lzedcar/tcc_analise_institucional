# Diagnóstico de Desempenho Institucional no TJSP com Ciência de Dados
Análise de padrões, gargalos e perfis operacionais com técnicas de agrupamento

## Descrição

Este repositório contém os códigos, dados e resultados desenvolvidos no Trabalho de Conclusão do Curso MBA em Ciência e Análise de Dados - USP/Esalq.
O projeto utiliza dados públicos disponibilizados pela Corregedoria-Geral da Justiça do Tribunal de Justiça de São Paulo (TJSP), contendo indicadores institucionais agregados por órgão judicial.
Os dados representam o desempenho acumulado entre maio de 2023 e abril de 2024, conforme informações extraídas do painel Justiça em Números do CNJ, disponibilizadas pela Corregedoria-Geral da Justiça do TJSP.
O objetivo do projeto é identificar padrões de desempenho, gargalos operacionais e desigualdades estruturais entre órgãos judiciais do TJSP, por meio de técnicas de análise exploratória, agrupamento (clustering) e modelagem como recurso complementar para teste de hipóteses.

## Estrutura do repositório

<pre> ```bash tcc_analise_institucional/ ├── dados/ # Bases originais e tratadas │ ├── TJSP_tbl_correg.csv │ └── TJSP_com_clusters.csv ├── scripts/ # Scripts Python com numeração sequencial │ ├── 00_etapas_limpeza_manual.py │ ├── 01_carregar_limpar_dados.py │ ├── 02_analise_exploratoria.py │ ├── 03_clustering.py │ ├── 04_mapeamento_clusters.py │ ├── 05_cluster_por_grau.py │ ├── 06_exportar_com_clusters.py │ ├── 07_modelo_preditivo.py │ └── 08_outliers_iad.py ├── graficos/ # Visualizações geradas │ ├── clusters_pca.png │ ├── clusters_por_grau.png │ ├── clusters_por_municipio.png │ ├── correlacao_indicadores.png │ ├── cotovelo_kmeans.png │ ├── distribuicao_iad.png │ ├── medias_por_cluster.png │ └── modelo_preditivo_iad.png ``` </pre>

## Tecnologias utilizadas

- Python 3.12+
- Spyder 5.5.1 (IDE utilizada para desenvolvimento)
- Pandas — manipulação de dados
- NumPy — operações numéricas
- Matplotlib — visualizações gráficas
- Seaborn — visualizações estatísticas
- Scikit-learn — clustering, regressão e normalização
- os — manipulação de caminhos
- warnings — controle de alertas

## Metodologia aplicada

- Importação e padronização de base de dados bruta (.csv)
- Renomeação e tratamento de colunas com símbolos e formatos inconsistentes (%, vírgulas, nulos)
- Detecção e tratamento de valores ausentes
- Análise estatística descritiva (distribuições, medidas de tendência, dispersão)
- Visualização gráfica de distribuições e correlações
- Análise de correlação entre variáveis institucionais
- Aplicação de agrupamento não supervisionado (K-Means) para identificação de perfis institucionais
- Avaliação da quantidade ideal de clusters (Elbow Method)
- Visualização da distribuição de clusters por município (gráfico de barras)
- Regressão linear auxiliar para avaliar relações entre indicadores e o IAD
- Identificação de outliers extremos com base no Índice de Atendimento à Demanda (IAD)
- Exportação da base enriquecida com clusters para reuso ou reprodução

## Principais descobertas

- Evidência de desigualdade estrutural entre órgãos com desempenhos extremos no TJSP
- Identificação de três perfis institucionais distintos por meio de agrupamento (K-Means)
- Os três clusters foram rotulados como: Alta Carga/Baixo Desempenho, Perfil Intermediário/Instável e Alta Eficiência/Alta Produtividade, com base nas médias de IAD, produtividade e carga processual.
- Órgãos com baixos valores de IAD revelam potenciais gargalos operacionais
- Órgãos com valores de IAD excepcionalmente altos representam possíveis boas práticas ou exceções sistêmicas
- A distribuição dos clusters apresenta forte relação com a classificação por grau (G1, G2, JE, TR)
- A regressão linear indicou que os indicadores operacionais disponíveis explicam apenas uma fração do desempenho (R² ≈ 0,11), sugerindo influência de fatores estruturais e qualitativos não incluídos na base
- Visualizações revelaram variabilidade significativa entre unidades judiciais em produtividade e carga de trabalho
- A análise não supervisionada permitiu organizar os órgãos por similaridade de funcionamento, revelando padrões institucionais
- As comparações entre grupos mostraram que estrutura e carga impactam diretamente o desempenho judicial

## Limitações

- A base utilizada reflete apenas dados agregados e quantitativos, sem variáveis institucionais detalhadas (como número de magistrados, recursos disponíveis ou tempo médio por processo).
- Além disso, o conjunto inclui diferentes tipos de unidades (varas, CEJUSCs, juizados, etc.), mas sem uma variável explícita de tipo funcional, o que limita a comparabilidade entre os registros.
- A base não contém variáveis geográficas explícitas (como coordenadas), o que limita representações espaciais mais precisas dos dados.
- Os dados abrangem um período limitado (maio/2023 a abril/2024), o que restringe a análise a uma janela temporal específica.
- O agrupamento foi realizado com base exclusivamente em variáveis numéricas, sem considerar aspectos qualitativos relevantes da atuação institucional.
- A modelagem preditiva foi empregada como instrumento auxiliar e apresentou explicabilidade limitada, não sendo adequada para prognósticos individuais.
- Não foi possível realizar inferências causais, apenas associações exploratórias com base nos padrões observados.
  
## Referências

Conselho Nacional de Justiça [CNJ]. Justiça em Números – Painel de Estatísticas. Brasília, DF, Brasil. Disponível em: <https://justica-em-numeros.cnj.jus.br/painel-estatisticas/>. Acesso em: 03 de junho de 2025.
Da Ros, Luciano. 2015. O custo da Justiça no Brasil: uma análise comparativa exploratória. Newsletter. Observatório de elites políticas e sociais do Brasil. NUSP/UFPR, v.2, n. 9, julho. p. 1-15. ISSN 2359-2826. < http://observatory-elites.org/wp-content/uploads/2012/06/newsletter-Observatorio-v.-2-n.-9.pdf>
Domingos, P. 2015. The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World. New York, NY, USA: Basic Books.
Favero, L. P.; Belfiore, P. 2017. Manual de Análise de Dados: Estatística e Modelagem Multivariada com Excel, SPSS e Stata. São Paulo, SP, Brasil: Elsevier. 660 p.
Hastie, T.; Tibshirani, R.; Friedman, J. 2009. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. 2. ed. New York, NY, USA: Springer. 745 p.
Pedregosa, F. et al. 2011. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12: 2825–2830.< http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>
Porto, A. C. 2019. O impacto da transformação digital no judiciário brasileiro: uma análise da adoção de tecnologias no sistema judicial. Revista Eletrônica do TRT da 9ª Região, 9(96): 1–17.
Ribeiro, M. V. M. (2024). A importância da inteligência artificial no poder judiciário brasileiro. REVISTA DELOS, 17(61), e2804. <https://doi.org/10.55905/rdelosv17.n61-142>. Acessado em: 15 de março de 2025.
Russell, S.; Norvig, P. 2021. Artificial Intelligence: A Modern Approach. 4. ed. Upper Saddle River, NJ, USA: Pearson.
Silva, G. C.; Macedo, T. S. 2020. Aplicações de ciência de dados no setor público: um estudo de caso no Poder Judiciário. Revista de Administração Pública e Gestão Social, 12(3): 229–245. <https://doi.org/10.21118/apgs.v12i3.8204>

## Autor(a)

Este repositório foi desenvolvido por Luciana Zedan de Carvalho como parte do Trabalho de Conclusão do Curso MBA em Ciência e Análise de Dados — USP/Esalq 2025.
