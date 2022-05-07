def isPowerOfTwo(n):

    def divideByTwo(n):
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 2:
            return False
        else:
            return divideByTwo(n / 2)

    return divideByTwo(n)

print(isPowerOfTwo(-1))
print(isPowerOfTwo(1))
print(isPowerOfTwo(2))
print(isPowerOfTwo(3))
