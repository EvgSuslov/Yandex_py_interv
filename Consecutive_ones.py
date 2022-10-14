# It is required to find the longest sequence of units in a binary vector and output its length.
#input: 1           output: 1
#       5
#       1
#       0
#       1
#       0



import sys
count = sys.stdin.readline().strip()

result = 0
max = 0
for i in range(int(count)):
    el = sys.stdin.readline().strip()
    if el == '1':
        result += 1
    else:
        if max < result:
            max = result
        result = 0

print(max if max > result else result)
