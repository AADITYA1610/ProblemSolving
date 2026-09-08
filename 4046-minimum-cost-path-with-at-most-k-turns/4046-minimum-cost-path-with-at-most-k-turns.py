import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        INF = float('inf')

        dist = [[[[INF] * (k + 1) for _ in range(4)] for _ in range(n)] for _ in range(m)]

        heap = [(grid[0][0], 0, 0, -1, 0)]

        while heap:
            cost, r, c, direction, turns = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return cost

            if direction != -1 and cost > dist[r][c][direction][turns]:
                continue

            for nd, (dr, dc) in enumerate(directions):
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_turns = turns

                    if direction != -1 and direction != nd:
                        new_turns += 1

                    if new_turns > k:
                        continue

                    new_cost = cost + grid[nr][nc]

                    if direction == -1:
                        old_cost = INF
                    else:
                        old_cost = dist[nr][nc][nd][new_turns]

                    if new_cost < old_cost:
                        dist[nr][nc][nd][new_turns] = new_cost
                        heapq.heappush(
                            heap,
                            (new_cost, nr, nc, nd, new_turns)
                        )

        return -1