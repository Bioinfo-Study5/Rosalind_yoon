seq = "GTAGAAAGACGATATCGACTAAATCAGAGCCCTTAATTGCTCGTCAGGCCCTGACATGGCGGGTCAGTAAGAACCTGGAAGACATACATGGCGCTACCGGCTACGAGTTGTGGGTCGGTGACAATTCACCGAATACCCCCTCACCGAATCAGAGATGCAGCGGCCGAGTATGGTCACAAGCATCCCCCTCCGTCACCCTAGTAGAGTGAATAGTTTCTCCTTACCATCGACGTCACAGTCAATAATGCTTGGCAACACTAGAGCAGGTAAAAATATTAGAAGATCCCTCGAGTATCAATAGTAGATGAACCACTTTATTGGTCTTTATTAACCGTGTGATTCTTAGGCGGCCGTTCCGGTTCGACTGGTAGTGGGAGCACTACTTCATGGGTGGTGTAAGCGCGCTAGCAACATCTATACCTGTTTCGGTTTCCCATATGATTGTTCTTATTAGCAGTTCGAGCTCATTGTACGTAGCGACCGTTACTCCTATCTACTCCAGCGCGGTACTTTGTCCTGGTGAGAACTGCATATTTGTAAAGCGTTCTCAGAGGCCCTAGCGCTCGCCCGGGACTAACTGCCGCGTTGGAGGGCTGCGCAACAGGGGGGGATCTGGCGTGTAACATACTTTCAGATTACACACCATCGAGCTACTGTGTCTACTTGCATGCAACGGTTAAAAACACTCCATACTGGAACAGATGATTGTTCCGGAGGGCGGGGATGTACAAAAACGATTCGAGATGGAGAGCACAAGAGCGGCAGGTCATGTCTGTTCTTAAAGCATTCCGTGTGGTCAAAAGTCTCCAGTAGTAGGGGGTTGCTA"

dna = {"A":"T", "T":"A", "G":"C", "C":"G"}
data = ""

seq_r = seq[::-1]
for base in seq_r:
    data += dna[base]

print(data)