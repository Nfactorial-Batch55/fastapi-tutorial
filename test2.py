# Given a 32-bit signed integer, reverse digits of an integer.
#
#
# Example 1:
#
#
# Input: 123
# Output: 321
# Example 2:
#
#
# Input: -123
# Output: -321
# Example 3:
#
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when
# the reversed integer overflows.

# def task(number: int) -> int:
#     if not (2**31 <= number <= 2**31 - 1):
#         return 0
#     minus = False
#     if number < 0:
#         number = -1 * number
#         minus = True
#     number = str(number)[::-1]
#     number = int(number)
#     if minus:
#         return -1*number
#     return number
# def task(number: int) -> int:
#
#     res = 0
#     c = 10
#     minus = False
#     if number < 0:
#         number = abs(number)
#         minus = True
#     while number != 0:
#         a = number % 10
#         number //= 10
#         res = res * c + a
#     if not (-2**31 <= res <= 2**31 - 1):
#         return 0
#     if minus:
#         return -1 * res
#     return res
#
# print(task(2**31-2))
# print(2**31 - 1 )

# Longest Substring Without Repeating Characters
# Question: Write a function that finds the length of the longest substring without repeating characters.
# Example:
# length_of_longest_substring("abcabcbb")  # Output: 3 ("abc")
# length_of_longest_substring("bbbbb")     # Output: 1 ("b")
# length_of_longest_substring("pwwkew")    # Output: 3 ("wke")

def length_of_longest_substring(substring: str) -> str:
    subs = ''
    for s in substring:
        for ss in subs:
            if s == ss:
                subs = s
        subs = subs + s

    print(len(subs), f'("{subs}")')


length_of_longest_substring("pwwkew")
