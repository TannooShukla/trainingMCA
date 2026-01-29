n = int(input("Enter number: "))                 # diamond radius
size = 2 * n + 1      # square size (always odd)

for i in range(size):
    for j in range(size):

        # square border
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")

        # filled diamond inside
        elif abs(i - n) + abs(j - n) <= n:
            print("*", end="")

        else:
            print(" ", end="")
    print()
