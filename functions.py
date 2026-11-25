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

seq = "ATGCGTACGTTAGC"
print("GC content:", round(gc_content(seq), 2))
print("Complement:", complement(seq))
print("Reverse complement:", reverse_complement(seq))