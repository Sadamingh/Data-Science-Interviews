def climbStairs(n):
    if n == 1 or n == 2:
        return n

    f1, f2 = 1, 2

    for i in range(n-2):
        f1, f2 = f2, f1 + f2

    return f2

print(climbStairs(5))
