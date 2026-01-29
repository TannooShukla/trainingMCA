n = int(input("Enter width: "))

for i in range(3):
    for j in range(n):
        if (i == 0 and j % 4 == 0) or \
           (i == 1 and j % 2 == 1) or \
           (i == 2 and j % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
