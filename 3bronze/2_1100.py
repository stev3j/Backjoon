# 짝수번째 줄이라면 0, 2, 4, 6
# 홀수번째 줄이라면 1, 3, 5, 7

chess = [input() for _ in range(8)]

odd = [0, 2, 4, 6]
even = [1, 3, 5, 7]

F = 0

for line in range(8):
    if line%2 == 0:
        for i in odd:
            if chess[line][i] == 'F':
                F += 1
    else:
        for i in even:
            if chess[line][i] == 'F':
                F += 1

print(F)