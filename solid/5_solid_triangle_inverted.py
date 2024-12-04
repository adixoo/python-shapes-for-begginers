#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

print("Solid Triangle Inverted")
print("")

height = int(input("Enter triangle height: "))

for i in range(height,0,-1):
    if (i == height):
        print("* " * height)
    else:
        spaces = " " * (height - i)
        star =  "* " * i
        print(spaces + star + spaces)

    