dna = "ATGCGT"

# 1. Print each base on its own line
for base in dna:
    print(base)

# 2. Count G and C using a loop
gc = 0
for base in dna:
    if base == "G" or base == "C":
        gc = gc + 1
print("G and C bases:", gc)

# 3. Print each position number with its base
for i in range(len(dna)):
    print(i, dna[i])