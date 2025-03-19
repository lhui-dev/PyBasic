result = 0
for i in range( 101):
    result += i
print(result)


# 1! + 2! + 3! + 4! + ... + n!
total = 0
start = 1
while start <= 4:
    result = 1
    m = 1
    while m<=start:
        result *= m
        m += 1
    total += result
    start+=1
print(total)
