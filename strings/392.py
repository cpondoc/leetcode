class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # General Idea: Keep incrementing and check
        # Runtime: O(n)
        # Memory: O(1)
        if (len(s) == 0): return True
        if (len(t) == 0): return False
        index = 0
        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
                if (index == len(s)):
                    return True
        return False