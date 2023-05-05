# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

def maxVowels(self, s: str, k: int) -> int:
    vowels = set(("a", "e", "i", "o", "u"))
    maxV = 0
    tempCount = 0
    for i in range(len(s)):
        if i >= k:
            # Tail of the window
            if s[i - k] in vowels:
                tempCount -= 1
            # Head of the window
        if s[i] in vowels:
            tempCount += 1
        maxV = max(maxV, tempCount)
    return maxV