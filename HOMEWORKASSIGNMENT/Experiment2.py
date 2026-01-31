class Solution:
    def getMinMax(self, arr):
        # Initialize minimum and maximum with first element
        minimum = arr[0]
        maximum = arr[0]

        # Traverse the array
        for i in range(1, len(arr)):
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i] > maximum:
                maximum = arr[i]

        return [minimum, maximum]


# -------- Driver Code --------
arr = [6, 8, 9, 2, 1]

obj = Solution()
result = obj.getMinMax(arr)

print("Minimum and Maximum:", result)




arr = [6, 8, 9, 2, 1]

obj = Solution()
result = obj.getMinMax(arr)

print("Minimum and Maximum:", result)
