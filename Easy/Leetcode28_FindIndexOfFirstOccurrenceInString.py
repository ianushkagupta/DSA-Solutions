# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution(object):
    def strStr(self, haystack, needle):
        position = 0
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    position = i
                    break
                else:
                    continue
            return position
        else:
            return -1
        
        