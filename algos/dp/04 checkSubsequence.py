def isSubsequence(s, t):

    f = 0

    for char in s:

        if char in t[f:]:
            f += t[f:].index(char) + 1
        else:
            return False

    return True

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
