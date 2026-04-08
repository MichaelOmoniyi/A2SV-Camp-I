n = int(input())
a = list(map(int, input().split())) * 2

maxRest, rest = 0, 0

for i in range(len(a)):
    if a[i] == 1:
        rest += 1
    else:
        maxRest = max(maxRest, rest)
        rest = 0
print(maxRest)