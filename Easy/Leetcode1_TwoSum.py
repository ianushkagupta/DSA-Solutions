# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_num = 0
        res = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    sum_num = nums[i] + nums[j]
                    if sum_num == target:
                        res.append(i)
                        res.append(j)
                        return(res)