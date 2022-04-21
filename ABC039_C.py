import io
import sys

_INPUT = """\
6
WBWBWWBWBWBWWBWBWWBW
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  a=S.index('WW')
  b=S[a+2:].index('WW')
  if b==3:
    if a==6: print('Fa')
    elif a==4: print('So')
    elif a==2: print('La')
    else: print('Si')
  else:
    if a==4: print('Do')
    elif a==2: print('Re')
    else: print('Mi')