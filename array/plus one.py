from typing import List

"""
you are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

def plusOne(self, digits: List[int]) -> List[int]:
    size = len(digits)
    carry = 1
    for i in range(size -1, -1 ,-1):
        sum = digits[i] + carry
        if sum <= 9:
            digits[i] = sum
            break
        elif sum > 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,carry)
    print(digits)

while True:
    l = input().split(',')
    l = [int(a) for a in l]
    plusOne(1,l)