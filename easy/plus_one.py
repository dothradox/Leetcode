digits = [1, 9, 9, 9]
if digits.count(9) == len(digits):
    digits = [0] * len(digits)
    digits.insert(0, 1)
    print(digits)
    quit()
for i, n in enumerate(digits[::-1]):
    if n != 9:
        digits[-(i + 1)] += 1
        print(digits)
        break
    if n == 9:
        digits[-(i + 1)] = 0
