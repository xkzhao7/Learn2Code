def write_to_file(name, text):
    with open(name + ".txt", "a") as x:
        x.write(text)
    with open(name + ".txt") as x:
        print(x.read())
if __name__ == "__main__":
    write_to_file("bank", "This is a bank!")