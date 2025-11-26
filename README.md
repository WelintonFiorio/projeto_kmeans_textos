# Projeto: K-Means em Textos – Reuters C50

## 1. Descrição do projeto

Este projeto implementa um sistema de **clusterização de textos** usando o algoritmo **K-Means**, inspirado na abordagem do Apache Mahout, mas implementado totalmente em Python.

O objetivo é agrupar documentos da base **Reuters C50** em clusters semanticamente coerentes, analisando os principais termos de cada grupo.

A pipeline do projeto inclui:

1. Carregamento dos arquivos de texto (`load_data.py`)
2. Pré-processamento e vetorização TF-IDF (`preprocess.py`)
3. Execução do K-Means (`kmeans_model.py`)
4. Análise dos clusters e exportação de resultados (`cluster_analysis.py`)
5. Execução completa via `main.py`
6. Análise automática dos clusters via `analisar_clusters.py`

---

## 2. Estrutura do projeto

```
projeto_kmeans_textos/
│
├── data/                           ← Base de dados
│   └── C50/
│       ├── C50train/
│       └── C50test/
│
├── src/                            ← Código fonte
│   ├── __init__.py
│   ├── load_data.py
│   ├── preprocess.py
│   ├── kmeans_model.py
│   ├── cluster_analysis.py
│   ├── main.py
│   └── analisar_clusters.py      ← Script para análise automática dos clusters
│
├── output/                         ← Resultados do K-Means
│   └── clusters.csv
│
├── venv/                           ← Ambiente virtual
├── requirements.txt                ← Dependências Python
└── README.md                        ← Este arquivo
```

---

## 3. Requisitos

* Python 3.8 ou superior
* Biblioteca **pandas**
* Biblioteca **numpy**
* Biblioteca **scikit-learn**
* Biblioteca **beautifulsoup4** (para conversão dos arquivos `.sgm`)

### Instalação das dependências

No terminal do PyCharm ou CMD:

```bash
pip install pandas numpy scikit-learn beautifulsoup4
```

Opcionalmente, se quiser adicionar gráficos e NLP avançado:

```bash
pip install matplotlib nltk
```

---

## 4. Base de dados

O projeto utiliza a base **Reuters C50**, que possui 50 categorias de textos.

### Download

1. Link oficial (UCI / CMU):
   [https://archive.ics.uci.edu/ml/machine-learning-databases/reuters21578-mld/reuters21578.tar.gz](https://archive.ics.uci.edu/ml/machine-learning-databases/reuters21578-mld/reuters21578.tar.gz)

2. Extraia o arquivo. Dentro dele haverá a pasta `C50` com:

```
C50/
├── C50train/
└── C50test/
```

3. Copie a pasta `C50` para a pasta `data/` do projeto:

```
projeto_kmeans_textos/data/C50/
```

### Caminhos completos

* Treino: `data/C50/C50train`
* Teste (opcional): `data/C50/C50test`

---

## 5. Como executar

1. Abra o PyCharm e selecione este projeto.
2. Certifique-se de que a pasta `data/C50/C50train` está corretamente posicionada.
3. Certifique-se de ter instalado as dependências (`requirements.txt`).
4. Execute o arquivo principal:

```bash
python src/main.py
```

O pipeline completo será executado:

* Carregamento dos textos
* Vetorização TF-IDF
* Clusterização com K-Means (10 clusters por padrão)
* Exibição dos top termos de cada cluster
* Geração do CSV `output/clusters.csv` com os arquivos e seus clusters

---

## 6. Análise dos clusters

Após a execução do pipeline, você pode analisar os clusters de forma automática com:

```bash
python src/analisar_clusters.py
```

O script irá:

1. Carregar o CSV `output/clusters.csv`
2. Listar os clusters encontrados
3. Mostrar alguns arquivos de cada cluster
4. Exibir um exemplo do conteúdo de cada cluster
5. Permitir interpretação semântica dos agrupamentos

### Observações

* Ajuste o parâmetro `n_clusters` no `main.py` conforme necessidade
* Verifique se os arquivos da mesma categoria ficaram agrupados juntos
* Use os termos principais de cada cluster para interpretar o tema semântico

---

## 7. Explicação dos arquivos

### 7.1 `load_data.py`

* Função `carregar_textos(base_path)`
* Lê todos os arquivos `.txt` da pasta base_path
* Retorna listas com os textos e seus caminhos

### 7.2 `preprocess.py`

* Função `vetorizar_textos(textos, max_features=5000)`
* Converte os textos em uma matriz TF-IDF
* Retorna a matriz e o vetor `vectorizer` para análise dos termos

### 7.3 `kmeans_model.py`

* Função `rodar_kmeans(X, n_clusters=10)`
* Executa o algoritmo K-Means sobre a matriz TF-IDF
* Retorna o modelo treinado e os labels de cluster

### 7.4 `cluster_analysis.py`

* Função `mostrar_top_termos(kmeans_model, vectorizer, n_top=15)`

* Exibe os principais termos de cada cluster

* Função `salvar_resultados(arquivos, labels, output_path="output/clusters.csv")`

* Salva um CSV com o nome do arquivo e o cluster correspondente

* Cria automaticamente a pasta `output/` se não existir

### 7.5 `main.py`

* Integra todas as funções anteriores
* Roda todo o pipeline de uma vez
* Exibe os clusters e salva resultados em `output/clusters.csv`

### 7.6 `analisar_clusters.py`

* Analisa automaticamente o CSV de clusters
* Lista arquivos por cluster
* Mostra exemplos de textos para interpretação semântica

---

## 8. Saída esperada

* CSV com cada arquivo e seu cluster: `output/clusters.csv`
* Console exibindo os **principais termos de cada cluster**, exemplo:

```
Cluster 0: market, trade, sales, company, growth
Cluster 1: government, policy, foreign, minister, relations
Cluster 2: match, team, win, season, coach
...
```

* Console exibindo arquivos e exemplos de textos para análise semântica via `analisar_clusters.py`

---

## 9. Observações finais

* O projeto é modular e facilmente expansível
* Parâmetros ajustáveis: `n_clusters` (K-Means), `max_features` (TF-IDF)
* Possível integração com visualização (Matplotlib, Plotly)
* Automatização da análise dos clusters já incluída

---

## 10. Autor

* **Welinton Fiorio Inoch**
* Projeto acadêmico de clusterização de textos usando Python
