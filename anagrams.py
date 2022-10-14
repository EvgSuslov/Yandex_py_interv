import sys
 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
j=sorted(j)
s=sorted(s)
if j == s:
	print(1)
else:
	print(0)
