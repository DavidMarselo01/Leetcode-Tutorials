import math
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Start with left, right = 0
        # How do we evaluate if the window of len(t) is valid?
        #We look at the window and compare the count to ABC
        #Then, if it equals, we check the minimum
        
        def is_part(count1, count2):
            for key, value in count1.items():
                if key in count2:
                    if count2[key] < count1[key]:
                        return False
                else:
                    return False
            return True
        
        minimum_sub_len = math.inf
        output = ''
        t_count = Counter(t)
        
        left = 0
        for right in range(len(s) + 1):
            while is_part(t_count, Counter(s[left:right])):
                if len(s[left:right]) < minimum_sub_len:
                    minimum_sub_len = len(s[left:right])
                    output = s[left:right]
                left += 1
                
        return output
        
        