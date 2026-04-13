class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed))
        stack = [] # stacks time it takes to get to the target
        print(pos_speed)

        for i in range(len(pos_speed) - 1, -1, -1):
            stack.append((target - pos_speed[i][0]) / pos_speed[i][1])
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
            print(stack)

        return(len(stack))
