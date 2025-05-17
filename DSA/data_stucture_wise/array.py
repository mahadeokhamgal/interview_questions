from typing import List
from collections import defaultdict
import collections

def allPaths(arr):
    ans = []
    N = len(arr)
    M = len(arr[0])
    moves = [
        (1, 0),
        (0, 1)
    ]
    def backTrack(x, y, path):
        if x == M-1 and y == N-1:
            ans.append(path[::])
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N:
                path.append([nx, ny])
                backTrack(nx, ny, path)
                path.pop()
    
    backTrack(0, 0, [])
    return ans

# print(allPaths([[1, 2, 3],[4, 5, 6]]))

def sort_zeros_n_ones(arr: list) -> list:
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            right -= 1
        else:
            left += 1
    
    return arr

# print(sort_zeros_n_ones([1,0,1,0,1,1,0,0,1,0]))

# LeetCode 209: Minimum Size Subarray Sum
def minSubArray(nums: list, target: int) -> int:
    best = float('infinity')
    left = 0
    currSum = 0

    for right in range(len(nums)):
        currSum += nums[right]

        while currSum - nums[left] >= target:
            currSum -= nums[left]
            left += 1
        
        if currSum >= target:
            best = min(best, right-left+1)

    return best if best != float('infinity') else -1

    """
    Brute FOrce
    totalSum = sum(nums)
    if totalSum < target:
        return -1
    
    best = len(nums)
    for i in range(len(nums)-1):
        currSum = nums[i]
        if currSum >= target: return 1
        for j in range(i+1, len(nums)):
            currSum += nums[j]
            if currSum >= target:
                best = min(best, j - i + 1)
                break
    
    return best
    """

# print(minSubArray([1, 2, 3, 4, 5], 11))

def subarrayWithSum(nums: List[int], k: int) -> List[int]:
    """Brute force
    for i in range(len(nums)-1):
        currSum = nums[i]
        for j in range(i+1, len(nums)):
            currSum += nums[j]
            if currSum == k:
                return [i, j]
    
    return [-1, -1]
    """
    """Optimised"""
    
    prefixSum = 0
    preFixSumMap = {0: -1}

    for idx, num in enumerate(nums):
        prefixSum += num

        if (prefixSum - k) in preFixSumMap:
            return [preFixSumMap[prefixSum-k]+1, idx]
        if prefixSum not in preFixSumMap:
            preFixSumMap[prefixSum] = idx
            
    return [-1, -1]

# print(subarrayWithSum([1,2,3,4], 7))
    # IP - [1,2,3,4], 7, OP - [2, 3]
def minTaps(n: int, ranges: List[int]) -> int:
    maxReachFrom = [0] * (n + 1)
    
    for idx, currRange in enumerate(ranges):
        left = max(0, idx - currRange) #make sure to keep left >= 0
        right = min(n, idx + currRange) # to keep right <= n
        maxReachFrom[left] = max(maxReachFrom[left], right) # we reach as farther as possible
    
    tapsUsed = 0
    currEnd = 0
    nextEnd = 0
    
    for i in range(n + 1):
        if i > nextEnd:
            return -1# no water zone.
        if i > currEnd: # if we reach a point where previos tap dosn't reach then use new tap
            tapsUsed += 1
            currEnd = nextEnd
        nextEnd = max(nextEnd, maxReachFrom[i])
    return tapsUsed

# print(minTaps(6, ranges = [0, 2, 0, 0, 1, 0, 2]))

def positiveNegativePairs(nums: List[int]):
    seen = set()
    done = set()
    ans = []
    for num in nums:
        if abs(num) not in done and -num in seen:
            ans.extend([-abs(num), abs(num)])
            done.add(abs(num))
        else:
            seen.add(num)
    return ans

# print(positiveNegativePairs([1,3,6,-2,-1,-3,2,7]))

def minimize_cash_flow(balances: dict):
    transactions = []

    def getMaxReceiver():
        return max(balances, key = lambda x: balances[x])

    def getMaxDebt():
        return min(balances, key = lambda x: balances[x])

    while True:
        maxReceiver = getMaxReceiver()
        maxDebter = getMaxDebt()

        amount = min(balances[maxReceiver], -balances[maxDebter])
        if amount < 1e-9:
            break
        balances[maxReceiver] -= amount
        balances[maxDebter] += amount

        transactions.append(f"{maxDebter} pays amount {amount} to {maxReceiver}")

    return transactions

IP = {
    "Alice": -70,
    "Bob": 50,
    "Charlie": -30,
    "David": 60,
    "Eve": -10
}

# print(minimize_cash_flow(IP))

def count_special_nodes(adj: List[List[int]], values: List[int]) -> int:
    # start create stack. push element 0, add it to ans += 1 as uniq. now go one by one dfs ysing stack as per below.
    # use stack and traverse over each node using adjecency list, keep track of seen nodes, if already seen node then don't visit.
    # keep track of path and if you're moving back/backtracking then pop that node/val from path.
    # everytime you visit new node if path is uniq/non duplicate vals then ans += 1.
    # Go till stack has elements.
    stack = [(0, set())]  # Each item: (current_node, set of values seen so far)
    ans = 0

    while stack:
        node, seen = stack.pop()
        val = values[node]

        if val in seen:
            continue

        new_seen = seen.copy()
        new_seen.add(val)
        ans += 1

        for neighbor in adj[node]:
            stack.append((neighbor, new_seen))

    return ans

# print(count_special_nodes([[1, 2], [3, 4], [], [], []], [1, 2, 3, 4, 5]))  
# print(count_special_nodes([[1, 2], [3, 4], [], [], []], [1, 2, 1, 4, 2]))  

def longestSubsequence(arr): # GFG
    dp = [0] * 10
    maxLength = 0

    for num in arr:
        currentMax = 0
        digitsOfCurrentElement = [False] * 10

        temp = num
        while temp > 0:
            digit = temp % 10
            digitsOfCurrentElement[digit] = True
            currentMax = max(currentMax, dp[digit] + 1)
            temp //= 10

        for digit in range(10):
            if digitsOfCurrentElement[digit]:
                dp[digit] = currentMax

        maxLength = max(maxLength, currentMax)

    return maxLength

def commonDigitLongestSubsequence(nums: List[int]) -> int: # Mine
    N = len(nums)
    dp = [0] * N
    dp[N-1] = 1
    longestDict = collections.defaultdict(int)
    ans = 0
    
    for i in range(N-1, -1, -1):
        num = nums[i]
        currMax = 1
        while num:
            digit = num % 10
            currMax = max(currMax, longestDict[digit]+1)
            num //= 10
        
        num = nums[i]
        while num:
            digit = num % 10
            longestDict[digit] = currMax
            num //= 10
        
        ans = max(ans, currMax)
    
    return ans

# print(longestSubsequence([12, 23, 34]))
# print(commonDigitLongestSubsequence([12, 23, 34]))

# print(longestSubsequence([30, 20, 10]))
# print(commonDigitLongestSubsequence([30, 20, 10]))

# print(longestSubsequence([65, 54, 43, 32, 21, 10]))
# print(commonDigitLongestSubsequence([65, 54, 43, 32, 21, 10]))

# print(longestSubsequence([91, 82, 73, 10]))
# print(commonDigitLongestSubsequence([91, 82, 73, 10]))

def colourful_knapsack(m, x, weights, colours):
    f = defaultdict(int)
    for idx in range(len(weights)):
        if f[colors[idx]] > 0:
            f[colors[idx]] = min(f[colors[idx]], weights[idx])
        else:
            f[colors[idx]] = weights[idx]
    
    cost = 0
    heap = [-w for w in f.values()]
    heapq.heapify(heap)
    while m > 0:
        el = -heapq.heappop(heap)
        cost += el
        m -= 1
    
    return -1 if cost > x else x - cost

print(colourful_knapsack(3, 10, [3, 4, 2, 5, 1], [1, 2, 3, 1, 2]))