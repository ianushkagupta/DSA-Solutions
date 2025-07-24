# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        k = 0 

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[k] = nums[i]
                k = k+1

        return k
        