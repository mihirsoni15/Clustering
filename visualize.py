#import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_pairwise(df):
    # Creating Seaborn PairGrid and display it with streamlit
    fig = sns.pairplot(df[['Age', 'Annual_Income', 'Spending_Score']])
    st.pyplot(fig)

def plot_clusters(df, x_col, y_col, cluster_col):
    # Creating a figure
    fig, ax = plt.subplots()
    sns.scatterplot(
        x=x_col, 
        y=y_col, 
        data=df, 
        hue=cluster_col, 
        palette='Spectral',   # "Spectral" or "coolwarm" for appealing visuals
        ax=ax
    )
    ax.set_title("Customer Clusters")
    st.pyplot(fig)

def plot_elbow(k_values, wss_scores):
    fig, ax = plt.subplots()
    ax.plot(k_values, wss_scores, marker='o', color='purple')
    ax.set_xlabel("No. of Clusters")
    ax.set_ylabel("Within-Cluster Sum of Squares (WSS)")
    ax.set_title("Elbow Plot for KMeans")
    st.pyplot(fig)
