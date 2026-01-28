n = int(input("Enter pyramid height: "))

width = 2 * n + 1

for i in range(n + 1):
    for j in range(width):

        # Box border
        if i == 0 or i == n or j == 0 or j == width - 1:
            print("*", end="")

        # Filled pyramid
        elif j >= (n - i) and j <= (n + i):
            print("*", end="")

        else:
            print(" ", end="")
    print()




 




