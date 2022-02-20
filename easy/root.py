num = 126
root = 1
for i in range(10):
    root = 0.5 * (root + (num / root))
print(root)
