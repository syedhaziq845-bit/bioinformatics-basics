dna = "ATGCGTACGTTAGC"

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

gc_percent = (g + c) / len(dna) * 100

print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)
print("GC content:", round(gc_percent, 2), "%")