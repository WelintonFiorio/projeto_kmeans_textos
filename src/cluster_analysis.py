# src/cluster_analysis.py

import pandas as pd

def mostrar_top_termos(kmeans_model, vectorizer, n_top=15):
    """
    Mostra os n_top termos mais importantes de cada cluster.
    """
    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans_model.cluster_centers_.argsort()[:, ::-1]

    clusters_info = []
    for i in range(kmeans_model.n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :n_top]]
        clusters_info.append(f"Cluster {i}: {', '.join(top_terms)}")
    return clusters_info

def salvar_resultados(arquivos, labels, output_path="output/clusters.csv"):
    """
    Salva um CSV com os arquivos e seus clusters.
    """
    df = pd.DataFrame({"arquivo": arquivos, "cluster": labels})
    df.to_csv(output_path, index=False)
