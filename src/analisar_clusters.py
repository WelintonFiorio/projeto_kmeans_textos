import pandas as pd

# 1️⃣ Carregar o CSV com os clusters
df = pd.read_csv("output/clusters.csv")

# 2️⃣ Listar clusters únicos
clusters = sorted(df['cluster'].unique())
print(f"Clusters encontrados: {clusters}")

# 3️⃣ Mostrar alguns arquivos de cada cluster
for c in clusters:
    print(f"\n=== Cluster {c} ===")
    # Mostra 5 primeiros arquivos do cluster
    arquivos = df[df['cluster'] == c]['arquivo'].head(5).tolist()
    for arq in arquivos:
        print(arq)

# 4️⃣ (Opcional) abrir o conteúdo de um arquivo para ver o texto
exemplo_arquivo = df[df['cluster'] == 0]['arquivo'].iloc[0]
with open(exemplo_arquivo, 'r', encoding='latin1') as f:
    print("\nConteúdo de exemplo do Cluster 0:\n")
    print(f.read())
