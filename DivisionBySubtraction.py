# DivisionBySubtraction
# 28 November 2016
# By turinturambar22


def division(num, div):
    i = 0
    while num >= div:
        num -= div
        i += 1
    if num == 0:
        return i
    elif num != 0:
        return i, num


