dna = "ATGGCCATTGTAATGGGCCGCTGA"

counts = {}
for i in range(0, len(dna) - 2, 3):
    codon = dna[i:i+3]
    if codon in counts:
        counts[codon] = counts[codon] + 1
    else:
        counts[codon] = 1

for codon in counts:
    print(codon, counts[codon])