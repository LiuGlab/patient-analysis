"""
This module counts the number of lines in standard input
Input: a string
Output: total number of lines
"""

import sys

count = 0
for line in sys.stdin:
         count = count+ 1
print(count, "lines in standard input")
