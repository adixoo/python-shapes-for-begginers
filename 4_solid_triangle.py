#          * 
#         * *
#        * * *
#       * * * *
#      * * * * *

print("Solid Triangle")
print("")

height = int(input("Enter triangle height: "))

for i in range(1,height + 1):
    spaces = ""
    if (i == height):
        pass
    else:
        spaces = " " * (height - i)
    star = "* " * i
    print(spaces + star)

