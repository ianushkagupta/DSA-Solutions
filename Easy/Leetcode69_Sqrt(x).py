# https://leetcode.com/problems/sqrtx/description/
class Solution(object):
    def mySqrt(self, x):
        i = 1
        res = 0
        while i**2 <= x:
            if i**2 == x:
                res = i
                break
            else:
                res = i
                i = i+1

        return res

        

            
            
