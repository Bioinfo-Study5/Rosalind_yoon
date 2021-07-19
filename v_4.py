a = int(input("a: "))
while a > 9999:
    a = int(input("a(<9999): "))
    print(a)

b = int(input("b: "))
while (b <= a) or (b >= 10000):
    b = int(input("b(a<b<10000): "))


sum = 0
for i in range(a, b+1):
    if i % 2 == 1:
        sum += i

print(sum)





