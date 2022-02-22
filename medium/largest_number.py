from functools import cmp_to_key

nums = [3, 30, 34, 9]
# Changing integer into string for concatenation
# NOTE: map(str,nums) can be used in place of this

# for i, n in enumerate(nums):
#     nums[i] = str(n)

# Compare concatenated numbers as string to be used as the key
def compare(n1, n2):
    if n1 + n2 > n2 + n1:
        print("\t-1")
        return -1
    else:
        print("\t1")
        return 1


nums = sorted(map(str, nums), key=cmp_to_key(compare))

print(str(int("".join(nums))))
