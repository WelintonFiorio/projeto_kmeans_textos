# src/kmeans_model.py

from sklearn.cluster import KMeans

def rodar_kmeans(X, n_clusters=10, max_iter=200, random_state=42):
    """
    Executa KMeans sobre a matriz TF-IDF e retorna o modelo treinado e os rótulos.
    """
    kmeans = KMeans(
        n_clusters=n_clusters,
        init="k-means++",
        max_iter=max_iter,
        random_state=random_state
    )
    kmeans.fit(X)
    labels = kmeans.labels_
    return kmeans, labels
