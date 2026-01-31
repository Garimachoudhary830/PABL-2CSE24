class Solution:
    def reverseArray(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr



obj = Solution()
arr = [1, 4, 3, 2, 6, 5]
print(obj.reverseArray(arr))
