class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        # Count characters in s
        for char in s:
            seen[char] = seen.get(char, 0) + 1

        # Remove counts using t
        for char in t:
            if char not in seen:
                return False

            seen[char] -= 1

            if seen[char] < 0:
                return False

        return True