from collections import deque

def maxMin(arr, k):
    n = len(arr)
    dq = deque()
    ans = float('-inf')

    for i in range(n):
        # Remove out-of-window indices
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain increasing order
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        dq.append(i)

        # Window ready
        if i >= k - 1:
            ans = max(ans, arr[dq[0]])

    return ans
