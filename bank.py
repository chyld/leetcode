class Solution:
    def totalMoney(self, n: int) -> int:
        days, weeks = n % 7, (n // 7) + 1
        part1 = [28 + (7 * w) for w in range(weeks)]
        part2 = range(days + weeks, 7 + weeks)
        return sum(part1) - sum(part2)
