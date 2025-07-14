def str_to_float(s):
    l = s.split(".")
    x = int(l[0])
    if len(l) > 1:
        if x > 0:
            x += int(l[1])/(10**len(l[1]))
        else:
            x -= int(l[1])/(10**len(l[1]))
    return x
if __name__ == "__main__":
    for number in ["1.27", "3002", "-5.9","-5.73357"]:
        print(str_to_float(number))