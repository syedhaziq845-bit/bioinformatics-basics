from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

Entrez.email = input("Enter your email (NCBI asks for it): ")

handle = Entrez.efetch(db="nuccore", id="NM_000546", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

print("ID:", record.id)
print("Description:", record.description)
print("Length:", len(record.seq))
print("GC content:", round(gc_fraction(record.seq) * 100, 2), "%")

SeqIO.write(record, "tp53.fasta", "fasta")
print("Saved tp53.fasta")