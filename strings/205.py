class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # General Idea: Keep two hash tables: one for frequency of each character. Keep track of frequency for each character.
        # Run-time: O(n)
        # Memory: O(n)
        s_chars = dict()
        s_arr = [int] * len(s)
        t_chars = dict()
        t_arr = [int] * len(t)
        for i in range(len(s)):
            if s[i] in s_chars:
                s_chars[s[i]] += 1
            else:
                s_chars[s[i]] = 1
            
            s_arr[i] = s_chars[s[i]]    
            
            if t[i] in t_chars:
                t_chars[t[i]] += 1
            else:
                t_chars[t[i]] = 1
            
            t_arr[i] = t_chars[t[i]]
        new_char_map = dict()
        for i in range(len(t_arr)):
            if (s_arr[i] != t_arr[i]):
                return False
            if s[i] in new_char_map:
                if new_char_map[s[i]] != t[i]:
                    return False
            new_char_map[s[i]] = t[i]
        return True