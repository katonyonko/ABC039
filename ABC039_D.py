import io
import sys

_INPUT = """\
6
4 4
##..
##..
..##
..##
4 4
###.
####
..##
..##
4 4
###.
##.#
..##
..##
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import itertools
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  S=[[0 if S[i][j]=="." else 1 for j in range(W)] for i in range(H)]
  ans=[[1]*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if S[i][j]==0:
        for k,l in itertools.product([-1,0,1],[-1,0,1]):
          if 0<=i+k<H and 0<=j+l<W:
            ans[i+k][j+l]=0
  tmp=[[0]*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if ans[i][j]==1:
        for k,l in itertools.product([-1,0,1],[-1,0,1]):
          if 0<=i+k<H and 0<=j+l<W:
            tmp[i+k][j+l]=1
  flag=0
  for i in range(H):
    for j in range(W):
      if S[i][j]!=tmp[i][j]: flag=1
  if flag==1: print('impossible')
  else:
    print('possible')
    for i in range(H):
      print(*["." if ans[i][j]==0 else "#" for j in range(W)], sep='')