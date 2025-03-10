class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        result = [0, 1]  
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > result[1]:
                    result[1] = current_length
                    result[0] = left
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand_around_center(i, i)
            
            expand_around_center(i, i+1)
                
        return s[result[0]:result[0] + result[1]]