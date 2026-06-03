class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        reversed_str = clean_text[::-1]
        if clean_text == reversed_str:
            return True
        return False