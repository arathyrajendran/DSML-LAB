import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans


df = pd.read_csv('https://raw.githubusercontent.com/jiss-sngce/CO_3/main/jkcars.csv')


print("===== First 5 Rows of Dataset =====")
print(df.head())
print("\nShape of Data:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())


new_df = df[['Volume', 'Weight', 'CO2']]


sil_scores = []
clusters = range(2, 11)

for k in clusters:
    kmeans_k = KMeans(n_clusters=k, random_state=10)
    kmeans_k.fit(new_df)
    cluster_labels = kmeans_k.predict(new_df)
    sil = silhouette_score(new_df, cluster_labels)
    sil_scores.append(sil)


silhouette_table = pd.DataFrame({
    'K': list(clusters),
    'Silhouette Score': sil_scores
})
print("\n===== Silhouette Scores Table =====")
print(silhouette_table)


plt.figure(figsize=(10, 5))
plt.plot(clusters, sil_scores, marker='o', linestyle='--', color='b')
plt.title('Silhouette Score vs K')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.xticks(range(2, 11))
plt.grid(True)
plt.show()

wess = []
for k in clusters:
    kmeans_k = KMeans(n_clusters=k, random_state=10)
    kmeans_k.fit(new_df)
    wess.append(kmeans_k.inertia_)


wess_table = pd.DataFrame({
    'K': list(clusters),
    'WESS': wess
})
print("\n===== WESS Table =====")
print(wess_table)


plt.figure(figsize=(10, 5))
plt.plot(clusters, wess, marker='o', linestyle='--', color='r')
plt.title('Elbow Method (WESS) vs K')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WESS")
plt.xticks(range(2, 11))
plt.grid(True)
plt.show()


kmeans_model = KMeans(n_clusters=3, random_state=10)
kmeans_model.fit(new_df)
cluster_labels = pd.Series(kmeans_model.predict(new_df))


print("\n===== Cluster Counts =====")
print(cluster_labels.value_counts())


df2 = pd.concat([df, cluster_labels], axis=1)
df2.columns = list(df.columns) + ['label']


print("\n===== Final Data with Cluster Labels =====")
print(df2.head())
