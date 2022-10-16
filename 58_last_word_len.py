'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.s = s
        i = len(s)-1 #start from end of str
        le = 0
        
        while s[i]==' ': # -1 to str pos
            i-=1
        while  i >= 0 and s[i] != " ": #if it is the word
            le += 1# len of word
            i -= 1#-1 to str pos
        return le
