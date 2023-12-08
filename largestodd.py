class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(1, len(num) + 1):
            if num[-i] in {"1", "3", "5", "7", "9"}:
                return num[: -i + 1] if i > 1 else num[:]
        return ""


s = Solution()
for n in ["52", "4206", "35427"]:
    print("-" * 50)
    print(n, s.largestOddNumber(n))
