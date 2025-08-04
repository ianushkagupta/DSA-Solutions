# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        num = 0
        place = 1
        for i in range(len(digits)-1,-1,-1):
            num = (digits[i]*place) + num
            place = place*10

        num = num + 1
        res = []
        for i in range(len(str(num))):
            res.append(int(str(num)[i]))
        
        return res
