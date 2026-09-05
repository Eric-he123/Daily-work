# 哈希表
# 思路：从已经查看过的数字中找是否有能与当前数字配对的，时间复杂度为 log(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            
            if need in seen:
                return [seen[need], i]
            
            seen[num] = i
