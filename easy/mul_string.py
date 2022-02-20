num1 = "2"
num2 = "3"
string = ""


def str_to_int(num):
    int_num = 0
    for i in num:
        int_num = (int_num * 10) + ((ord(i)) % 48)
    return int_num


result = str_to_int(num1) * str_to_int(num2)


def int_to_str(str):
    while True:
        result, remainder = divmod(result, 10)
        string = chr(ord("0") + remainder) + string
        if result == 0:
            break


print((string))
