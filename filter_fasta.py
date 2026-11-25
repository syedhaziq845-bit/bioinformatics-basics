from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

high_gc = []
for record in SeqIO.parse("sequences.fasta", "fasta"):
    gc = gc_fraction(record.seq) * 100
    if gc > 52:
        high_gc.append(record)

SeqIO.write(high_gc, "high_gc.fasta", "fasta")
print("Saved", len(high_gc), "sequences")