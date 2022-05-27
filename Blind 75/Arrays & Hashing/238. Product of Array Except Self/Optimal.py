#Time Complexity: O(n)
#Space Complexity: O(1)
#Note: Result array is not considered extra space, therefore it is O(1) Space
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            result[i] = prefix
            
        postfix = 1
        for i in range(len(result) - 1, -1, -1):
            if i == 0:
                result[i] = postfix
                continue
            result[i] = (postfix * result[i-1])
            postfix *= nums[i]
        return result