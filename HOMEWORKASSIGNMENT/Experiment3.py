class Solution:
    def kthSmallest(self, arr, k):
        # Sort the array
        arr.sort()
        
        # Return kth smallest element
        return arr[k - 1]



arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

obj = Solution()
result = obj.kthSmallest(arr, k)

print("Kth smallest element is:", result)
