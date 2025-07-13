class Solution:
    def fib(self, n: int) -> int:
        """
        if n==0:
            return 0
        if n==1:
            return 1
        left=self.fib(n-1)
        right=self.fib(n-2)
        return left+right
        """
        if n<2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]