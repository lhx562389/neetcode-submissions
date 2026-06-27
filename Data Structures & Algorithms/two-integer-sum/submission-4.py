class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, n in enumerate(nums):
            diff=target-n

            if diff in result:
                return [result[diff],i] #return the result key and the index
            result[n]=i
        