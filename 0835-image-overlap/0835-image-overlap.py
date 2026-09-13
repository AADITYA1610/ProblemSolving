from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones1 = []
        ones2 = []

        # Store coordinates of 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))

                if img2[r][c] == 1:
                    ones2.append((r, c))

        # Count how many pairs give the same translation
        shifts = defaultdict(int)

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1

                shifts[(dr, dc)] += 1

        # Maximum number of overlapping 1s
        return max(shifts.values(), default=0)