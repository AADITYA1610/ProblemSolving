class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_finish = max(land_finish, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, water_finish)

                water_finish = waterStartTime[j] + waterDuration[j]
                land_finish_2 = max(water_finish, landStartTime[i]) + landDuration[i]
                ans = min(ans, land_finish_2)

        return ans