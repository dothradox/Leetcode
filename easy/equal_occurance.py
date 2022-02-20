s = "abacbcdd"
hashmap = {}
for i in s:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1
value_list = list((hashmap.values()))
if value_list.count(value_list[0]) == len(value_list):
    print(True)
else:
    print(False)
# for i in range(len(hashmap) - 1):
#     if hashmap[i] != hashmap[i + 1]:
#         print(False)
# print(True)
