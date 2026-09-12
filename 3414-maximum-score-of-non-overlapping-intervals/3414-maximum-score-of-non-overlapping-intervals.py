class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

   
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        arr.sort()

        n = len(arr)

        
        import bisect

        starts = [x[0] for x in arr]
        nxt = [0] * n

        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect.bisect_right(starts, r)

      
        dp = [
            [(0, ()) for _ in range(n + 1)]
            for _ in range(5)
        ]

    
        for k in range(1, 5):
            for i in range(n - 1, -1, -1):

            
                skip_score, skip_indices = dp[k][i + 1]

            
                l, r, w, original_index = arr[i]

                take_score, take_indices = dp[k - 1][nxt[i]]

                take_score += w
                take_indices = tuple(
                    sorted((original_index,) + take_indices)
                )

              
                if take_score > skip_score:
                    dp[k][i] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[k][i] = (skip_score, skip_indices)

                else:
                   
                    if take_indices < skip_indices:
                        dp[k][i] = (take_score, take_indices)
                    else:
                        dp[k][i] = (skip_score, skip_indices)

        return list(dp[4][0][1])