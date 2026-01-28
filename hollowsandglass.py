n= int(input("Enter the number of rows: "))


# Upper inverted hollow pyramid
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        if i == n or j == 1 or j == 2*i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower hollow pyramid
for i in range(2, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        if i == n or j == 1 or j == 2*i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
