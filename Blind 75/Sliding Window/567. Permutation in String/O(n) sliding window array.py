class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def create_count_array(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return count
        
        if len(s1) > len(s2):
            return False
        
        s1_count = create_count_array(s1)
        #it is len(s1) - 1 because I want to start with one less char than len(s1)
        #Then, in the for loop i can add the len(s) char and count it
        s2_sub_count = create_count_array(s2[0:len(s1) - 1])
        
        left = 0
        for right in range(len(s1), len(s2) + 1):
            left_char_index = ord(s2[left]) - ord('a')
            right_char_index = ord(s2[right - 1]) - ord('a')
            s2_sub_count[right_char_index] += 1
            if s2_sub_count == s1_count:
                return True
            s2_sub_count[left_char_index] -= 1
            left += 1
            
        return False
        
		


