genes = ["BRCA1", "TP53", "EGFR"]

print(genes[0])
print(len(genes))

genes.append("MYC")
print(genes)

for gene in genes:
    print("Gene:", gene)

lengths = [1863, 393, 1210]
print(sum(lengths))
print(max(lengths))
print(min(lengths))