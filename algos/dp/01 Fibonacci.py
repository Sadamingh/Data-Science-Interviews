def fib(n):

    if n == 0 or n == 1:
        return n

    f0, f1 = 0, 1

    for _ in range(2, n+1):
        f0, f1 = f1, f0 + f1

    return f1

print(fib(7))
