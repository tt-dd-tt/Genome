from tqdm import tqdm
import random
import string
import os

# Create a dummy file of 1MB and start every record with @
with open('dummyfile.fastq', 'w') as outfile:
    for i in tqdm(range(1000000)):
        # Write the first line starting with '@' and containing a random sequence
        outfile.write('@' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + '\n')

        # Write the second line containing the random sequence
        outfile.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=50)) + '\n')

        # Write the third line starting with '+'
        outfile.write('+' + '\n')

        # Write the fourth line containing random quality scores
        outfile.write(''.join(random.choices(string.ascii_uppercase + string.digits, k=50)) + '\n')
