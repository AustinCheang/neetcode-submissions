class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for xs in s:
            s_dict[xs] += 1

        for xt in t:
            if xt not in s_dict:
                return False
            s_dict[xt] -= 1
            if s_dict[xt] == 0:
                del s_dict[xt]

        return len(s_dict) == 0