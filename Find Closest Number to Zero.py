# 可以直接使用abs()，此题较为简单，但注意还要满足如果两个数字离0同样近，是要输出更大的那一个

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest_num = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(closest_num) or (abs(nums[i] == abs(closest_num)) and nums[i] > closest_num):
                closest_num = nums[i]
            
        return closest_num
