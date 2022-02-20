s = "a"
t = "aa"
t_sum = s_sum = 0
for i in s:
    s_sum += ord(i)
for i in t:
    t_sum += ord(i)
print(chr(t_sum - s_sum))

for i in range(len(t)):
    t_sum += ord(t[i])
    s_sum += ord(s[i])
print(chr(t_sum - s_sum))
