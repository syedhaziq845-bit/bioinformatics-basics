from Bio import Entrez, SeqIO

Entrez.email = input("Enter your email: ")

handle = Entrez.efetch(db="nuccore", id="NM_000546", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

for feature in record.features:
    if feature.type == "CDS":
        cds = feature.extract(record.seq)
        protein = cds.translate(to_stop=True)
        print("CDS length:", len(cds))
        print("Protein length:", len(protein))
        print("First 30 amino acids:", protein[:30])