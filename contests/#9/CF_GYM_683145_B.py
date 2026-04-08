for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    small = 0
    for i in range(1, n):
        if abs(nums[i]) < abs(nums[0]):
            small += 1

    median = n // 2
    if small <= median:
        print("YES")
    else:
        print("NO")