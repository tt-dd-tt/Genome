import csv
from Bio import SeqIO

# Open the FASTQ file
with open("dummyfile.fastq", "r") as fastq_file:
    # Create a CSV file to write the data to
    with open("dummyfile.csv", "w", newline="") as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)
        # Write a header row
        csv_writer.writerow(["name", "sequence", "quality"])

        # Iterate over the records in the FASTQ file
        for record in SeqIO.parse(fastq_file, "fastq"):
            # Write the record's data to the CSV file
            csv_writer.writerow([record.name, record.seq, record.letter_annotations["phred_quality"]])
