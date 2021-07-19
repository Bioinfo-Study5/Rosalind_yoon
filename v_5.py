f = open('rosalind_ini5.txt', 'r')
n = 0
for line in f:
    line = line.strip()
    if n % 2 == 1:
        print(line)
    n += 1

f.close()