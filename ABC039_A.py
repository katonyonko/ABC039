import io
import sys

_INPUT = """\
6
2 3 4
3 4 2
100 100 100
1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C=map(int,input().split())
  print(2*(A*B+B*C+C*A))