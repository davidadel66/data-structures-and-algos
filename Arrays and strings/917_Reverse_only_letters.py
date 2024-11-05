# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        right = len(s) - 1
        left = 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        while left <= (len(s) - 1):
            # print(left, right)
            if s[left].lower() in letters:
                while s[right].lower() not in letters:
                    right -= 1
                ans.append(s[right])
                right -= 1
            else:
                ans.append(s[left])
            left += 1
                

            
                            

        # print("".join(ans))

        return "".join(ans)
