sorted_2 = [3, 6, 7, 9]
sorted_1 = [1, 2, 4, 6, 8, 9]

i = 0
j = 0
new_sorted = []
for k in range(len(sorted_1 + sorted_2)):
    if i != len(sorted_1) and (sorted_1[i] <= sorted_2[j]):
        new_sorted.append(sorted_1[i])
        print(sorted_1[i], end=" ")
        i = i + 1
        print("i={}".format(i))
    else:
        new_sorted.append(sorted_2[j])
        print(sorted_2[j], end=" ")
        j = j + 1

        print("j={}".format(j))
