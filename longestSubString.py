__author__ = 'achau1'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = len(s) if 26 > len(s) else 26
        for i in range(r, 0, -1):
            l = range(r - i + 1)
            for j in l:
                if self.noRepeats(s[j: j+i]):
                    return len(s[j: j+i])

    def noRepeats(self, checkThisString):
        memo = []
        for c in checkThisString:
            if c in memo:
                return False
            else:
                memo.append(c)
        return True


s = "abcabcbb"
x = Solution()
print(x.lengthOfLongestSubstring(s))
print("Should be 3")

s = "bbbbb"
x = Solution()
print(x.lengthOfLongestSubstring(s))
print("Should be 1")


