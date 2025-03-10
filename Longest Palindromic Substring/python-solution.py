class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        
        # Initialize DP table
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        start = 0
        max_length = 1
        
        # Single letter palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for two letter palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for longer palindromes
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]