class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        answer = 0
        

        for house in houses:
            low = 0 
            high = len(heaters) - 1
            while low <= high:
                mid = (low + high) // 2

                if house == heaters[mid]:
                    break
                
                elif house > heaters[mid]:
                    low = mid + 1
                
                else: 
                    high = mid - 1


            if low <= high:
                continue
        
            leftDistance, rightDistance = 0, 0 
 
            if high >= 0:
                rightDistance = abs(house - heaters[high])
            else: 
                rightDistance = float('inf')

            if low < len(heaters):
                leftDistance = abs(house - heaters[low])
            else:
                leftDistance = float('inf')
            
            answer = max(answer, min(leftDistance, rightDistance))

        return answer
