n = int(input())
s = input()

permutations = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]
minRecolorNo = n
soln = ""

for p in permutations:
    count = 0
    cur = ""
    for i in range(n):
        if s[i] != p[i % 3]:
            count += 1
        cur += p[i % 3]
    
    if count < minRecolorNo:
        minRecolorNo = count
        soln = cur

print(minRecolorNo)
print(soln)