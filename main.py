#import necessary libraries
import streamlit as st
import pandas as pd
from data_loader import load_data
from clustering import apply_kmeans, get_silhouette_scores
from visualize import plot_clusters, plot_elbow

st.title("Unsupervised Customer Segmentation")

file = st.file_uploader("Upload mall_customers.csv", type=["csv"])
if file:
    df = load_data(file)

    st.write("### Data Preview")
    st.dataframe(df.head())

    features = ['Annual_Income', 'Spending_Score']
    df_subset = df[features]

    n_clusters = st.slider("Select number of clusters", 2, 10, 5)
    model, labels, wss = apply_kmeans(df_subset, n_clusters)

    df['Cluster'] = labels
    st.write("### Clustered Data")
    st.dataframe(df)

    st.write("### Cluster Visualization")
    plot_clusters(df, 'Annual_Income', 'Spending_Score', 'Cluster')

    st.write("### Elbow Plot (WSS)")
    k_range = range(3, 9)
    wss_scores = [apply_kmeans(df_subset, k)[2] for k in k_range]
    plot_elbow(k_range, wss_scores)

    st.write("### Silhouette Scores")
    sil_scores = get_silhouette_scores(df_subset, k_range)
    st.dataframe(pd.DataFrame(sil_scores, columns=['Clusters', 'Silhouette Score']))
