# https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
            
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count = count + 1
            elif count > 0:
                break

        return count
        