Last login: Sun Jul  3 22:39:01 on ttys001
Darwin Patrik-Svajda.local 20.6.0 x86_64
22:43  up 8 days, 10:20, 2 users, load averages: 4.04 3.32 46.13
 ~  cd Desktop/                                        Sun Jul  3 22:43:53 2022
 ~/Desktop                                             Sun Jul  3 22:43:55 2022
 ~/Desktop  pip install biopython                      Sun Jul  3 22:43:55 2022
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
Requirement already satisfied: biopython in /usr/local/lib/python3.9/site-packages (1.79)
Requirement already satisfied: numpy in /usr/local/lib/python3.9/site-packages (from biopython) (1.23.0)
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
 ~/Desktop  python                             754ms  Sun Jul  3 22:43:59 2022

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Sep  6 2021, 07:39:44) 
[GCC Apple LLVM 12.0.5 (clang-1205.0.19.59.6) [+internal-os, ptrauth-isa=deploy on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import gzip
>>> from Bio import SeqIO
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named Bio
>>> 
>>> with gzip.open("/Users/libor/Desktop/aaa.fastq.gz", "rt") as handle:
...     for record in SeqIO.parse(handle, "fastq"):
...         print(record)
... 
