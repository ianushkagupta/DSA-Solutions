# https://leetcode.com/problems/search-insert-position/description/
class Solution(object):

    def searchInsert(self, nums, target):
        a = 0 
        b = len(nums) - 1

        while a <= b:
            mid = (a+b) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                a = mid + 1
            else:
                b = mid - 1

        return a



            

        
        