# Task: count gold nuggets
# input: 2 stirngs: 1st - gold nuggets, 2nd - goldnuggets, stones, sand other
# output: int(number)

# input: ab 
# input: aabbdfjg
# output: 4

import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
 
result = 0
for ch in s:
    if ch in j:
        result += 1
 
print(result)
