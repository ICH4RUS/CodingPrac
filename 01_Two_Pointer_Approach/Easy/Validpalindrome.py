class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newst=""
        for i in s:
            if i.isalnum():
                news+=i
        return newst==newst[::-1]
    