class Solution:
    # Time: O(n + m) | Space: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        s1_freq = [0] * 26
        window_freq = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        # check if current window matches
        matches = 0
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1

        if matches == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right char
            right_char = ord(s2[i]) - ord('a')
            window_freq[right_char] += 1

            if window_freq[right_char] == s1_freq[right_char]:
                matches += 1

            elif window_freq[right_char] == s1_freq[right_char] + 1:
                matches -= 1

            # add left char
            left_char = ord(s2[i - len(s1)]) - ord('a')
            window_freq[left_char] -= 1

            if window_freq[left_char] == s1_freq[left_char]:
                matches += 1
            elif window_freq[left_char] == s1_freq[left_char] - 1:
                matches -= 1
        
        return matches == 26
            