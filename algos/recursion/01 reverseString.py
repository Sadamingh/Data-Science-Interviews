class Solution:
    def reverseString(self, s):
        self.swap(s, 0, len(s)-1)

    def swap(self, s, left, right):

        if left >= right: return

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        self.swap(s, left, right)

ans = Solution()
s = ["h","e","l","l","o"]
ans.reverseString(s)
print(s)
