#双指针，此时由于数组是肾虚排列的，所有可以通过在头尾同时查找

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return [left+1, right+1]
