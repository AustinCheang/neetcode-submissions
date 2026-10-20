class Solution:
    # Time: O(n) | Space: O(n)
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    # Time: O(n) | Space: O(n)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # step 1: find the length of upcoming word
            length_pos_end = i
            while s[length_pos_end] != "#":
                length_pos_end += 1
            length = int(s[i:length_pos_end])

            word_start_pos = length_pos_end + 1
            word = s[word_start_pos:word_start_pos+length]
            result.append(word)

            i = word_start_pos+length
        return result
        

            
