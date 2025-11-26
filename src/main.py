# src/main.py

from load_data import carregar_textos
from preprocess import vetorizar_textos
from kmeans_model import rodar_kmeans
from cluster_analysis import mostrar_top_termos, salvar_resultados

def main():
    # Caminho da base de dados
    base_path = "data/C50/C50train"

    # 1. Carregar textos
    print("Carregando textos...")
    textos, arquivos = carregar_textos(base_path)
    print(f"Total de documentos carregados: {len(textos)}")

    # 2. Pré-processamento e vetorizar
    print("Convertendo textos em TF-IDF...")
    X, vectorizer = vetorizar_textos(textos)
    print(f"Matriz TF-IDF criada: {X.shape}")

    # 3. Rodar KMeans
    print("Executando KMeans...")
    kmeans_model, labels = rodar_kmeans(X, n_clusters=10)
    print("KMeans finalizado!")

    # 4. Mostrar top termos
    print("\nPrincipais termos por cluster:")
    clusters_info = mostrar_top_termos(kmeans_model, vectorizer)
    for c in clusters_info:
        print(c)

    # 5. Salvar resultados
    salvar_resultados(arquivos, labels)
    print("\nResultados salvos em output/clusters.csv")

if __name__ == "__main__":
    main()
