dna = "ATGCGTACGTTAGC"

print(dna.lower())
print(dna[0:3])
print(dna[-1])

a_count = dna.count("A")
t_count = dna.count("T")
print(a_count + t_count)

print(dna + "AAA")