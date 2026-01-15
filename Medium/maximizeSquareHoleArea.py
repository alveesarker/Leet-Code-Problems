class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def longest_consecutive(arr):
            if not arr:
                return 0

            arr = sorted(arr)
            longest = curr = 1

            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                else:
                    longest = max(longest, curr)
                    curr = 1

            return max(longest, curr)

        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
