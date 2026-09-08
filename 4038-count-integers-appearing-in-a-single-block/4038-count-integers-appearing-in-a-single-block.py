class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        blocks = {}

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                blocks[nums[i]] = blocks.get(nums[i], 0) + 1

        ans = 0

        for x in blocks:
            if blocks[x] == 1:
                ans += 1

        return ans