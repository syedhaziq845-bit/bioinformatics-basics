codon_table = {
    "ATG": "M", "GCC": "A", "ATT": "I", "GTA": "V",
    "GGC": "G", "CGC": "R", "TGA": "*"
}

def transcribe(dna):
    return dna.replace("T", "U")

def translate(dna):
    protein = ""
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        amino = codon_table.get(codon, "?")
        if amino == "*":
            break
        protein = protein + amino
    return protein

gene = "ATGGCCATTGTAATGGGCCGCTGA"
print("RNA:", transcribe(gene))
print("Protein:", translate(gene))