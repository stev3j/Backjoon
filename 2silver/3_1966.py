import sys
input = sys.stdin.readline

def check(list, cnt, l, n):
    while True:
        if l == 1:
            print(cnt)
            break
        elif n != 0 and list[0] < max(list[1:]):
            list.append(list[0])
            del list[0]
            n -= 1
        elif n == 0:
            if list[0] < max(list[1:]):
                n = l-1
                list.append(list[0])
                del list[0]
            else:
                print(cnt)
                break
        elif list[0] >= max(list[1:]):
            del list[0]
            l -= 1
            n -= 1
            cnt += 1
    
t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    num = list(map(int, input().split()))
    cnt = 1
    check(num, cnt, l, n)


