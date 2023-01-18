from Bio import SeqIO
from sklearn.cluster import KMeans
import pandas as pd 

# Read the FASTQ file using biopython
records = SeqIO.parse("/home/ttsstt/Desktop/toys/genome/Genome/dummyfile.fastq", "fastq")
sequences = [str(record.seq) for record in records]

# Use k-means to cluster the sequences
kmeans = KMeans(n_clusters=5)
kmeans.fit(sequences)

# Print the cluster labels for each sequence
print(kmeans.labels_)
