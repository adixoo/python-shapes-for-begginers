#          * 
#         * *
#        *   *
#       *     *
#      * * * * *

print("Hollow Triangle")
print("")

height = int(input("Enter triangle height: "))

for i in range(1,height + 1):
    if i == height:  
        star = "* " * height
        print( star)
    elif i == 1:
        print(" " * (height - i) + "*") 
    else:
        print(" " * (height - i) + "*" + (" " * (2 * i - 3)) + "*")



