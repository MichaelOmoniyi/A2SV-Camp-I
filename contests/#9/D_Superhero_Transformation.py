s = input()
t = input()
vowels = "aeiou"

sLen = len(s)
tLen = len(t)

if sLen != tLen:
    print("No")
else:
    for i in range(sLen):
        if (s[i] in vowels and t[i] not in vowels) or (s[i] not in vowels and t[i] in vowels):
            print("No")
            break
    else:
        print("Yes")