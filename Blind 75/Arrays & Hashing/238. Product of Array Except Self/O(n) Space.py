#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_ls = []
        prefix = 1
        for number in nums:
            prefix *= number
            prefix_ls.append(prefix)
            
        postfix_ls = []
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            postfix_ls.append(postfix)
            
        postfix_ls.reverse()
            
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix_ls[i+1])
                continue
            elif i == len(nums) - 1:
                result.append(prefix_ls[i-1])
                continue
    
            prefix_mult = prefix_ls[i-1]
            postfix_mult = postfix_ls[i+1]
            
            result.append(prefix_mult * postfix_mult)
            
        return result
        
        
                
        