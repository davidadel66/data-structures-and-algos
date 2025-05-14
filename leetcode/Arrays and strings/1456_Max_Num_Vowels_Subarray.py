# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        numVowels = maxVowels = 0
        vowels = ['a','e','i','o', 'u']
        
        for right, _ in enumerate(s):
            # print(s[right])
            if s[right] in vowels:
                numVowels += 1
            # print(maxVowels)
            # print(s[left:right])
            while (right - left + 1) > k:
                if s[left] in vowels:
                    numVowels -= 1
                left += 1
            maxVowels = max(maxVowels, numVowels)


            # maxVowels = max(maxVowels, )

        return maxVowels