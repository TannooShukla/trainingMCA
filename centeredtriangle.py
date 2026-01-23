n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # spaces
    print(" " * (n - i), end="")
    # stars
    print("*" * (2 * i - 1))
    