class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[i+j for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (1 if word1[i-1]!=word2[j-1] else 0))
                
        # print(dp)
        return dp[len(word1)][len(word2)]