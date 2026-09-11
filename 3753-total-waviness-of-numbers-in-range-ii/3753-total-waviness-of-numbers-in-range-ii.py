class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def solve(x):
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))

            @lru_cache(None)
            def dp(pos, prev2, prev1, tight, started):
                if pos == len(digits):
                    return (1, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    new_tight = tight and d == limit

                    if not started and d == 0:
                        count, waviness = dp(
                            pos + 1, -1, -1, new_tight, False
                        )
                        total_count += count
                        total_waviness += waviness
                    else:
                        add = 0

                        if started and prev2 != -1:
                            if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                add = 1

                        count, waviness = dp(
                            pos + 1, prev1, d, new_tight, True
                        )

                        total_count += count
                        total_waviness += waviness + add * count

                return total_count, total_waviness

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)