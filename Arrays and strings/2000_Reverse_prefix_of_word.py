# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

 

# Example 1:

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
    
        letters = ans = []
        for idx, letter in enumerate(word):
            # print(idx, letter)
            if letter != ch[0]:
                letters.append(letter)
                # print(letters)
            else:
                letters.append(letter)
                # print(letters)
                ans = letters[::-1]
                # print(ans)
                ans.append(word[idx+1:])
                # print(ans)
                return "".join(ans)
        return "".join(ans)

