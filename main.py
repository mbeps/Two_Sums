class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map: dict[int] = {}
        for i, num in enumerate(nums):
            complement: int = target - num
            if (complement in num_map):
                return [num_map[complement], i]
            num_map[num] = i
        return []
 