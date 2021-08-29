class Solution:
    def find_max(self, arr):
        if not arr:
            return
        n = len(arr)
        l, r = 0, n - 1
        while l <= r:
            if l == r or l == r - 1:
                return max(arr[l], arr[r])
            m = (l + r) // 2
            if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
                return arr[m]
            if arr[m - 1] < arr[m]:
                l = m + 1
            else:
                r = m - 1
