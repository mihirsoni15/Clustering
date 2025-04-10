from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# To perform KMeans clustering and return model and labels
def apply_kmeans(df, n_clusters):
    model = KMeans(n_clusters=n_clusters)
    model.fit(df)
    return model, model.labels_, model.inertia_

# Calculating silhouette scores for different cluster counts
def get_silhouette_scores(df, cluster_range):
    scores = []
    for k in cluster_range:
        model = KMeans(n_clusters=k)
        labels = model.fit_predict(df)
        score = silhouette_score(df, labels)
        scores.append((k, score))
    return scores
