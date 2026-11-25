def is_valid(dna):
    for base in dna:
        if base not in "ATGC":
            return False
    return True

def gc_content(dna):
    gc = 0
    for base in dna:
        if base == "G" or base == "C":
            gc = gc + 1
    return gc / len(dna) * 100

def complement(dna):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    result = ""
    for base in dna:
        result = result + pairs[base]
    return result

def reverse_complement(dna):
    return complement(dna)[::-1]

def transcribe(dna):
    return dna.replace("T", "U")

codon_table = {
    "ATG": "M", "GCC": "A", "ATT": "I", "GTA": "V",
    "GGC": "G", "CGC": "R", "TGA": "*"
}

def translate(dna):
    protein = ""
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        amino = codon_table.get(codon, "?")
        if amino == "*":
            break
        protein = protein + amino
    return protein

seq = input("Enter a DNA sequence: ").upper().strip()

if seq == "" or not is_valid(seq):
    print("Invalid DNA sequence")
else:
    print("Length:", len(seq))
    print("GC content:", round(gc_content(seq), 2), "%")
    print("Reverse complement:", reverse_complement(seq))
    print("RNA:", transcribe(seq))
    print("Protein:", translate(seq))