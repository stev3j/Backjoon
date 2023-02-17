import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
y, m = 0, 0

for i in range(n):
    y += (list[i] // 30 + 1) * 10
    m += (list[i] // 60 + 1) * 15

if y < m: print('Y', y)
elif m < y: print('M', m)
else: print('Y M', y)