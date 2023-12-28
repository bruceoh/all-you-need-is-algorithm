class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            lv, li = nums[left]
            rv, ri = nums[right]
            if lv + rv > target:
                right -= 1
            elif lv + rv < target:
                left += 1
            else:
                if li > ri:
                    li, ri = ri, li
                return [li, ri]

        raise NotImplementedError


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
