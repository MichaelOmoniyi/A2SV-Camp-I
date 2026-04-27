class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.calendar.sort()
        left, right = 0, len(self.calendar) - 1

        while left <= right:
            mid = (left + right) // 2
            start, end = self.calendar[mid]

            if not (endTime <= start or startTime >= end):
                return False
            elif startTime < start:
                right = mid - 1
            else:
                left = mid + 1
        self.calendar.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)