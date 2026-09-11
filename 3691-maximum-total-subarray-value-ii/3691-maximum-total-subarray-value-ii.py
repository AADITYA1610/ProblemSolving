from typing import List
import heapq

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        self.log = [0] * (n + 1)

        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        m = self.log[n] + 1

        self.mx = [[0] * m for _ in range(n)]
        self.mn = [[0] * m for _ in range(n)]

        for i in range(n):
            self.mx[i][0] = nums[i]
            self.mn[i][0] = nums[i]

        for j in range(1, m):
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + half][j - 1]
                )

                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + half][j - 1]
                )

    def query(self, l, r):
        length = r - l + 1
        j = self.log[length]

        maximum = max(
            self.mx[l][j],
            self.mx[r - (1 << j) + 1][j]
        )

        minimum = min(
            self.mn[l][j],
            self.mn[r - (1 << j) + 1][j]
        )

        return maximum - minimum


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTable(nums)

        heap = []

        for l in range(n):
            value = st.query(l, n - 1)
            heapq.heappush(heap, (-value, l, n - 1))

        answer = 0

        for _ in range(k):
            neg_value, l, r = heapq.heappop(heap)

            answer -= neg_value

            if r > l:
                value = st.query(l, r - 1)
                heapq.heappush(heap, (-value, l, r - 1))

        return answer