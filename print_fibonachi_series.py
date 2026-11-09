def print_fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        print(a, end=" ")
        a, b = b, a + b

print_fibonacci(100)
