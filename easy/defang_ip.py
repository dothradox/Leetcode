address = "256.1.15.1"
split_address = address.split(".")
new_address = ""
for i in range(3):
    new_address = new_address + split_address[i] + "[.]"
new_address = new_address + split_address[3]
print(new_address)
