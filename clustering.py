import dask.dataframe as dd
from dask.distributed import Client
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

# Start a Dask cluster
client = Client()  # Start a local cluster

# Read data from CSV file
df = dd.read_csv("dummyfile.csv")

# Convert the sequence data to a numerical representation
# Here we are one-hot-encoding the sequences
df['sequence'] = df['sequence'].apply(lambda x: np.array([int(i) for i in x.split(',')], dtype=np.uint8), meta=('sequence', np.ndarray))

# Convert the dataframe to a numpy array
sequences = df[['sequence']].compute().values

# Initialize the k-means model with the desired number of clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(sequences)

# Get the cluster labels
labels = kmeans.labels_

# Plot the data using the cluster labels as colors
# Since the data is in one dimension, we can't plot it in 2D
# We can use the labels to observe the clusters
plt.scatter(range(len(labels)), labels, c=labels, cmap='rainbow')

# Show the plot in a separate window and save the picture to a file
plt.show()
plt
