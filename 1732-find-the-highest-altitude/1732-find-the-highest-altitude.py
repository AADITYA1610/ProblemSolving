class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for x in gain:
            altitude += x
            highest = max(highest, altitude)

        return highest