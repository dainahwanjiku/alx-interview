#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    total_oper = 0
    num_oper = 2
    while n > 1:
        while not n % num_oper:
            total_oper += num_oper
            n /= num_oper
        num_oper += 1
    return total_oper
