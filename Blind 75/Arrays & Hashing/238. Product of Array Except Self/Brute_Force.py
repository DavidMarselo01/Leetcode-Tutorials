#Time Complexity: O(n^2)
#Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        counter = 0
        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if counter != j:
                    cur *= nums[j]
            counter += 1
            result.append(cur)
        return result