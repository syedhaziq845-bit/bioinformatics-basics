dna = "ATGCGTACGTTAGC"
dna = dna.upper()

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

if a + t + g + c == len(dna):
    print("Valid DNA sequence")
else:
    print("Invalid: contains letters other than A, T, G, 
C")
dna = "ATGCXTA"