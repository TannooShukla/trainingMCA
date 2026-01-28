n = int(input("Enter the number of rows: "))

# Upper half (including middle line)
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower half (start from n-1 to avoid duplicate)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

