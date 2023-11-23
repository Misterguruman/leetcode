# https://leetcode.com/problems/palindrome-number/

def isPalindrome(self, x: int) -> bool:
    value = [x for x in str(x)]
    reversed_value = []
    reversed_value += value
    reversed_value.reverse()
    
    if value == reversed_value:
        return True

    return False