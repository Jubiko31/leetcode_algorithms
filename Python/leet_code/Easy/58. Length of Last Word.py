# ==============Length of Last Word================

# ? Given a string s consisting of words and spaces, return the length of the last word in the string.
# ! A word is a maximal substring consisting of non-space characters only.

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split(' ')[-1])

# Runtime: 79.70% | Memory: 19.39%