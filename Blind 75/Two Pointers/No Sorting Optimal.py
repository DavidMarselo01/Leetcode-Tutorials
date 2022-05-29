#Time Complexity: O(n^2)
#Space Complexity: O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:       
        set_n = {}
        for i in range(len(nums)):
            set_n[nums[i]] = i
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in set_n and set_n[complement] != i and set_n[complement] != j:
                    cur_list = [nums[i], nums[j], complement]
                    cur_list = sorted(cur_list)
                    ans.add(tuple(cur_list))
                    
        return [list(x) for x in ans]