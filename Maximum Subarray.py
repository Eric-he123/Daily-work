# 核心问题是：遍历到 nums[i] 时，之前的子数组还值不值得继续保留？
# 如果之前的和是正数，继续连接会让当前和更大；
# 如果之前的和是负数，继续连接只会拖累当前元素，不如从 nums[i] 重新开始。
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum
