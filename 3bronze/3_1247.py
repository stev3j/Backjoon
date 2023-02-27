import sys
input = sys.stdin.readline

for _ in range(3):
    sum = 0
    for i in range(int(input())):
        n = int(input())
        sum += n
    if sum > 0: print('+')
    elif sum < 0: print('-')
    else: print('0')