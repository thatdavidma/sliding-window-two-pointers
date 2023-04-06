# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
		
def strStr(self, haystack: str, needle: str) -> int:
    # Basically sliding the window of needle length to check if the indexes match
    if len(needle) == 0:
        return 0
    elif len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i:len(needle)+i] == needle:
            return i
    return -1