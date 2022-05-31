from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #left, right pointing at the same thing
        #We calcutate the frequency counter
        # We look at the sum of the all characters with least frequecy and compare to k
        #if it is less than k, then we update max
        #if it is more than k, then we move left pointer until it is less than k
        
        left = 0
        max_sub = 0
        substring_freq = {}
        def sum_all_least_freq(count):
            most_freq_key = max(count, key = count.get)
            sum_freq = 0
            for key, value in count.items():
                if key != most_freq_key:
                    sum_freq += count[key]
                    
            return sum_freq
        for right in range(len(s)):
            substring_freq[s[right]] = 1 + substring_freq.get(s[right], 0)
            if sum_all_least_freq(substring_freq) <= k:
                max_sub = max(max_sub, len(s[left : right + 1]))
            else:
                while sum_all_least_freq(substring_freq) > k:
                    substring_freq[s[left]] -= 1          
                    # if substring_freq[s[left]] == 0:
                    #     del(substring_freq[s[left]])
                    left += 1
        return max_sub
                
        
