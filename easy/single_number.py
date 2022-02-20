nums = [2, 2, 1]
hashset = set(nums)
set_sum, num_sum = 0
for i in hashset:
    set_sum += i
for i in nums:
    num_sum += i
print((2 * set_sum) - num_sum)
