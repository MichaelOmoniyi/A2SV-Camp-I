class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Recursion
        def helpReverse(left, right):
            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]

            helpReverse(left + 1, right - 1)
        
        helpReverse(0, len(s) - 1)

        # Two point pointers
        # l, r = 0, len(s) - 1
        
        # while l < r:
            # swap elements
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1