class Solution:
    def maxProduct(self, nums):
        a = 0
        b = 0
        for n in nums:
            if n > a:
                a, b = n, a
            elif n > b:
                b = n
        return (a - 1) * (b - 1)


s = Solution()
nums = [10, 2, 5, 2]
print(nums, s.maxProduct(nums))

#
# watchexec -r -e py -- python max-prod.py
