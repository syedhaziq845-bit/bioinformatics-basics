from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("sequences.fasta", "fasta"):
    seq = record.seq
    print("ID:", record.id)
    print("Description:", record.description)
    print("Length:", len(seq))
    print("GC content:", round(gc_fraction(seq) * 100, 2), "%")
    print("Reverse complement:", seq.reverse_complement())
    print("Protein:", seq.translate(to_stop=True))
    print("-----")