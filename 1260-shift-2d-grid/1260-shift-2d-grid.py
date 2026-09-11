class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        k = k % (m * n)

        arr = []
        for row in grid:
            arr.extend(row)

        arr = arr[-k:] + arr[:-k]

        result = []
        for i in range(m):
            result.append(arr[i * n:(i + 1) * n])

        return result