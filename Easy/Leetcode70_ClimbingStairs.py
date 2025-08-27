# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        # n-1
        one_step = 2 
        # n-2
        two_step = 1

        for i in range(3,n+1):
            curentval = one_step + two_step

            two_step = one_step
            one_step = curentval

        return one_step