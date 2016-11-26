# PrimeCoder Module
# 18 November 2016
# Returns product of representative primes for each letter in message or takes product and splits into numbers
# By turinturambar22


class Key:
    NUMS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]


def encode(message, nums, letters):
    split_message = []
    result = 1
    for sym in message:
        split_message += sym
    for i in split_message:
        result *= nums[letters.index(i)]
    return result


def decode(message, nums, letters):
    result = ""
    i = 0
    while i < 26:
        if message % nums[i] == 0:
            result += letters[i]
            message = message / nums[i]
        else:
            i += 1
    return result
