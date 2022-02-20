s = "01:01:00AM"
if s[-2:] == "AM" and s[:2] == "12":
    print("00{}".format(s[2:-2]))
if s[-2:] == "PM" and s[:2] != "12":
    print("{}{}".format((int(s[:2]) + 12), s[2:-2]))
print(s[:-2])
