from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        time = 0

        for i in range(len(tickets)):
            queue.append(i)

        while tickets[k] != 0:
            tickets[queue[0]] -= 1
            time += 1
            if tickets[queue[0]] == 0:
                queue.popleft()
            else:
                queue.append(queue.popleft())
        return time