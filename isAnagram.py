class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if length of both strings are different, automatically false
        # because it is not an anagram
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        # check the frequencies of each strings
        freq = 1 # because the new string added to the dict will be counted as 1

        for i in range(len(s)):
            # if a character not found, return 0 so 1+0 = 1 -> first encounter of the string
            s_dict[s[i]] = freq + s_dict.get(s[i], 0)
            t_dict[t[i]] = freq + t_dict.get(t[i], 0)

        # check equality of both dictionary
        return s_dict == t_dict
