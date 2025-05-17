**Meesho**
**https://www.naukri.com/code360/interview-experiences/meesho/meesho-interview-experience-dec-2020-exp-0-2-years-2011**

R1. 
Q1. `Weighted Job Scheduling.`
Leetcode #1235. Maximum Profit in Job Scheduling.

You are given 'N' jobs with their start time 'Start', end time 'End' and profit 'Profit'. You need to tell the maximum profit you can obtain by performing these jobs such that no two jobs overlap.
Note: The start time of one job can be equal to the end time of another.
Eg. 1. OP - 140
Start  = [1, 3, 6]
End    = [3, 5, 9]
Profit = [20, 20, 100]

Eg. 2. OP - 120
Start  = [1, 2, 3, 3]
End    = [3, 4, 5, 6]
Profit = [50, 10, 40, 70]

```py
def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    groupedIntervals = sorted(zip(startTime, endTime, profit))
    
    @cache
    def backTrack(i):
        if i == len(groupedIntervals):
            return 0
        #no take
        res = backTrack(i+1)
        #take
        j = bisect.bisect(groupedIntervals, (groupedIntervals[i][1], -1, -1))
        #this is to find first index which doesn't overlap with currnet interval
        res = max(res, groupedIntervals[i][2] + backTrack(j))
    
        return res
    
    return backTrack(0)
```

Q2. `You are given an ‘M*N’ Matrix, You need to print all possible paths from its top left corner to the bottom right corner if given that you can either move right i.e from (i,j) to (i,j+1) or down i.e from (i, j) to (i+1, j).`
For Example :
IP = [[1 2 3],
      [4 5 6]]

For the above 2*3 matrix , possible paths are (1 2 3 6) , (1 2 5 6) , (1 4 5 6).
- Ans
```py
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
```

Q3. `Maximum sum of two non-overlapping subarrays of a given size.`
You are given an array/list ARR of integers and a positive integer ‘K’. Your task is to find two non-overlapping subarrays (contiguous) each of length ‘K’ such that the total sum of these subarrays is maximum.
IP - [2, 5, 1, 2, 7, 3, 0], k = 2
OP - 17
**Leetcode #1031: Maximum Sum of Two Non-Overlapping Subarrays.​**

```py
def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
    N = len(nums)
    fs = collections.defaultdict(int)
    prefixSum = sum(nums[:firstLen])
    for idx in range(firstLen, N):
        fs[idx] = prefixSum
        prefixSum += nums[idx]
        prefixSum -= nums[idx - firstLen]
    fs[N] = prefixSum
            
    def getMaxOut(i, j):
        best = 0
        for key in fs.keys():
            if not i <= key <= j:
                best = max(best, fs[key])
        
        return best

    prefixSum = sum(nums[:secondLen])
    ans = 0
    for j in range(secondLen, N):
        ans = max(ans, prefixSum + getMaxOut(j-secondLen, j+firstLen-1))
        prefixSum += nums[j]
        prefixSum -= nums[j-secondLen]
    
    ans = max(ans, prefixSum + getMaxOut(N-secondLen, N+firstLen-1))
    return ans
```

R2.
Q.1 **Minimum Character Deletion**
`You are given a string ‘STR’. You need to find and return the minimum number of characters to be deleted from ‘STR’ so that the frequency of each character in the string becomes unique.`
**Leetcode 1647**
```py
def minDeletions(s: str) -> int:
    seen = set()
    deletions = 0

    for freq in collections.Counter(s).values():
        while freq > 0 and freq in seen:
            freq -= 1
            deletions += 1
        seen.add(freq)

    return deletions
```

Q.2 **Pair with Given Sum in a Balanced BST**
`You are given the ‘root’ of a Balanced Binary Search Tree and an integer ‘target,’ you have to tell if there exists any pair of nodes such that the sum of their value is equal to the target.`
`More formally check if there exist any two distinct nodes, whose sum is equal to ‘target.’`
Leetcode # 653
```py
def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    seen = set()

    def recursion(node):
        if not node:
            return False
        elif k - node.val in seen:
            return True
        else:
            seen.add(node.val)
            return recursion(node.left) or recursion(node.right)
    
    return recursion(root)
```

Q.3. **Minimum Number Of Taps To Water Garden**
`The gardener wants to water the garden by opening the minimum number of taps. The garden is one-dimensional along the x-axis of length N i.e. the garden starts from point 0 and ends at point N. There are N + 1 tap located at points [0, 1, 2, …, N] in the garden.`
`You are given an integer N, and an array named “ranges” of size N + 1(0-indexed). The ith tap, if opened, can water the gardener from point (i - ranges[i]) to (i + ranges[i]) including both. The task is to find the minimum number of taps that should be open to water the whole garden, return -1 if the garden can not be watered.`
Leetcode # 1326
```py
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
```