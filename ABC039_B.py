import io
import sys

_INPUT = """\
6
1
981506241
390625
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=int(input())
  for i in range(10**3):
    if i**4==X:
      print(i)
      break