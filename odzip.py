import gzip
import shutil
with gzip.open('/Users/libor/Desktop/aaa.fastq.gz', 'rb') as f_in:
    with open('file.fastq', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)



