


print("Solid Diamond")
print("")

size = int(input("Enter size: "))

for i in list(range(1,size)) + list(range(size,0,-1)):
    if i == size:
        print("* " * i)
    else:
        spaces = " " * (size - i)
        print(spaces + "* " * i)