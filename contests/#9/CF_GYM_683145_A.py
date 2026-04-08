sound = "meow"

for _ in range(int(input())):
    n = int(input())
    soundStr = input().lower()
    j = 0
    charList = []

    if soundStr[0] != "m" or soundStr[-1] != "w":
        print("NO")
        continue
    
    for i in range(n):
        if not charList:
            charList.append(soundStr[i])
        else:
            if soundStr[i] != charList[-1]:
                charList.append(soundStr[i])
    soundStr = "".join(charList)

    if soundStr == sound:
        print("YES")
    else:
        print("NO")