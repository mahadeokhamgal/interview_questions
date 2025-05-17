# Samsung - https://www.naukri.com/code360/interview-experiences/samsung/samsung-interview-experience-by-anubhav-jain-on-campus-dec-2019-16

R1. Q1. Colourful Knapsack.
`You are given N stones, labeled from 1 to N. The i-th stone has the weight W[i]. There are M colors, labeled by integers from 1 to M. The i-th stone has the color C[i] (of course, an integer between 1 to M, inclusive). You want to fill a Knapsack with these stones. The Knapsack can hold a total weight of X. You want to select exactly M stones; one of each color. The sum of the weights of the stones must not exceed X. Since you paid a premium for a Knapsack with capacity X (as opposed to a Knapsack with a lower capacity), you want to fill the Knapsack as much as possible.`
`Write a program that takes all the above values as input and calculates the best way to fill the Knapsack – that is, the way that minimizes the unused capacity. Output this unused capacity.`
This one is in To do. - bit overhead.
```py
from collections import defaultdict
from typing import List

def colourful_knapsack(m: int, x: int, weights: List[int], colours: List[int]) -> int: # GPT
    from collections import defaultdict

    color_to_weights = defaultdict(list)
    for w, c in zip(weights, colours):
        color_to_weights[c].append(w)

    colors = list(color_to_weights.keys())
    n_colors = len(colors)

    dp = [set() for _ in range(m + 1)]
    dp[0].add(0)  # base case: 0 stones, 0 weight

    for color in colors:
        current_stones = color_to_weights[color]
        for k in range(m, 0, -1):
            for prev_weight in dp[k - 1]:
                for stone_weight in current_stones:
                    new_weight = prev_weight + stone_weight
                    if new_weight <= x:
                        dp[k].add(new_weight)

    if not dp[m]:
        return x  # No valid combination
    best_weight = max(dp[m])
    return x - best_weight

def colourful_knapsack(m, x, weights, colours): # doesn't work as we need to mimise x-cost and not cost
    
""" Greedy this gives max difference possible
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
"""
# Test Case 1: Basic Example
    "M": 3,
    "X": 10,
    "W": [3, 4, 2, 5, 1],
    "C": [1, 2, 3, 1, 2],
    "expected": 4

# Test Case 2: Exact Fit
    "M": 3,
    "X": 9,
    "W": [3, 3, 3],
    "C": [1, 2, 3],
    "expected": 0

# Test Case 3: Impossible to Fit
    "M": 2,
    "X": 3,
    "W": [2, 4, 5, 6],
    "C": [1, 1, 2, 2],
    "expected": -1

# Test Case 4: Multiple Options
    "M": 3,
    "X": 12,
    "W": [4, 3, 6, 5, 2, 3],
    "C": [1, 1, 2, 2, 3, 3],
    "expected": 1

# Test Case 5: Only One Stone per Color, Overweight
    "M": 3,
    "X": 7,
    "W": [2, 3, 4],
    "C": [1, 2, 3],
    "expected": -1
"""
```

R.2 Q.1. Longest Increasing Subsequence.
`The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.`
# https://leetcode.com/problems/longest-increasing-subsequence/description/
```py
 def lengthOfLIS(self, nums: List[int]) -> int:
    """Binary Search"""
    deck = []
    for num in nums:
        idxToInsert = bisect.bisect_left(deck, num)
        if idxToInsert == len(deck):
            deck.append(num)
        else:
            deck[idxToInsert] = num
            
    return len(deck)
        
    """# bottom up
    N = len(nums)
    dp = [1] * N
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)"""
    
    """dp
    N = len(nums)
    @cache
    def dfs(idx) -> int:
        if idx >= N:
            return 0
        runner = idx
        best = 1
        for runner in range(idx, N):
            if nums[runner] > nums[idx]:
                best = max(best, 1 + dfs(runner))
        
        return best

    return max(dfs(idx) for idx in range(N))
    """
```

# lets implement bisect left.
```py
def searchInsert(self, nums: List[int], target: int) -> int:
    # idea is to find number >= target
    def helper(left, right) -> int:
        if left >= right:
            return left
        
        mid = left + (right-left)//2
        if nums[mid] < target:
            return helper(mid+1, right)
        else:
            return helper(left, mid)
    
    return helper(0, len(nums))
```
Q.2 Find the top view of the tree.
`Given a binary tree, print the top view of it. The  output nodes can be printed in any order. Expected time complexity is O(n)`
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
```py
def topView(root: TreeNode):
    """BFS
    INF = 10 ** 10
    tops = {}
    leftMost = INF
    rightMost = -INF

    q = collections.deque([(0, root)])
    while q:
        for i in range(len(q)):
            idx, node = q.popleft()
            leftMost = min(leftMost, idx)
            rightMost = max(rightMost, idx)

            if idx not in tops:
                tops[idx] = node.val
            
            if node.left:
                q.append((idx-1, node.left))
            if node.right:
                q.append((idx+1, node.right))
    ans = []
    for i in range(leftMost, rightMost+1):
        ans.append(tops[i])

    return ans"""
    """DFS"""
    INF = 10 ** 10
    tops = {}
    leftMost = INF
    rightMost = -INF
    def dfs(idx, level, node):
        if not node:
            return
        if idx not in tops or tops[idx][1] < idx:
            tops[idx] = (node.val, level)
            leftMost = min(leftMost, idx)
            rightMost = max(rightMost, idx)
        
        dfs(idx-1, level-1, node.left)
        dfs(idx+1, level-1, node.right)
    dfs(0, 0, root)
    return [tops[i][0] for i in range(leftMost, rightMost+1)]
```

R3. Q.1. Merge Point Of Two Linked Lists
`To find the merging point of link list(Given pointers to the head nodes of 2 linked lists that merge together at some point, find the Node where the two lists merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.)`
