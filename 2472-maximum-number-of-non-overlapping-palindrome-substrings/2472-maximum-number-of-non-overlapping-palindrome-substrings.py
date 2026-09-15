class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i...j] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Length 1 palindromes
        for i in range(n):
            pal[i][i] = True

        # Build palindrome table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = maximum number of valid palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't use s[i-1]
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i-1
            for j in range(i):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]