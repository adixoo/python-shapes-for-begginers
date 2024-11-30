#      *       * 
#     * *     * * 
#    * * *   * * * 
#   * * * * * * * *

print("M - Pattern")
print("")


height = int(input("Enter size: "))

for i in range(1, height + 1):
    spaces = " " * (height - i)
    star = "* " * i
    print(spaces + star + spaces + spaces + star)