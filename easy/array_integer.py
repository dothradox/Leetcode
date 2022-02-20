num = [1, 2, 0, 0]
k = 34
result = 0
for i in num:
    result = result * 10 + i
result = result + k
print([int(x) for x in str(result)])
