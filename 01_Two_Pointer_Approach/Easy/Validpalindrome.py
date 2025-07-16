class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() #converting the string into lowercase 
        newst="" #string is immutable 
        for i in s:
            if i.isalnum(): #checks if all i is alphabets or numericals
                news+=i
        return newst==newst[::-1] #only returns values that are palindrome
    