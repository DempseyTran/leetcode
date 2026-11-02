class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = 0
        original_x = x = x
        while x > 0:
            digit = x % 10
            reversed_x = (reversed_x * 10) + digit
            x //= 10
        return reversed_x == original_x

        