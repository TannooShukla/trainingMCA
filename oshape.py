# print O shape star pattern
n = int(input("Enter the number of stars: "))
print("*" * n)  
for i in range(n - 2):
    print("*" + " " * (n - 2) + "*")
print("*" * n)
