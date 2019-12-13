""" Program - Miner
INPUT: n - rows count, m - colon count, k - mines count
row, col - coordinates of mines
OUTPUT: number - count of nearest mines, * - mine, . - no nearest mines in this place
EXAMPLE:
 IN
5 4 4
 1 1
 2 2
 3 2
 4 4
 OUT
* 2 1 . 
3 * 2 . 
2 * 3 1 
1 1 2 * 
. . 1 1 
"""
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)] # generate 0 in all rows
for i in range(k):  # input coordinates of mines
  row, kol = (int(i) - 1 for i in input().split())
  a[row][kol] = -1  # place at those coordinates -1

# iterate all matrix
for i in range(n):
  for j in range(m):
    if a[i][j] == 0:  # if no mine
      for di in range(-1, 2): # delta from i - in range[-1, 1]
        for dj in range(-1, 2): # delta from j - in range[-1, 1]
          ai = i + di # new coordinates of place
          aj = j + dj
          # (ai, aj)
          if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
            a[i][j] += 1  # check that this is in matrix and a mine 
                          # than addition with 1
# this is an output
for i in range(n):
  for j in range(m):
    if a[i][j] == -1: # if is mine, place "*""
      print("*", end = " ")
    elif a[i][j] == 0:  # if no mine nearest - place "."
      print(".", end = " ")
    else:   # in all another place the number of nearest mines
      print(a[i][j], end = " ")
  print() # new row
