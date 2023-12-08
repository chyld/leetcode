class Solution:
    def numberOfMatches(self, teams: int) -> int:
        matches = teams // 2 if teams % 2 else teams // 2
        advance = matches + 1 if teams % 2 else matches
        if advance > 1:
            return self.numberOfMatches(advance) + matches
        else:
            return matches
