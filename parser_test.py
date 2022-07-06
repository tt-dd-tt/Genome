import gzip
from Bio import SeqIO

with gzip.open("/Users/libor/Desktop/aaa.fastq.gz", "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        print(record)