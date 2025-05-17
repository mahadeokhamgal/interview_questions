SDE-1 Amazon
# https://www.naukri.com/code360/interview-experiences/amazon/amazon-interview-experience-by-anonymous-sde-1-dec-2020-exp-0-2-years-261?testVariant=0

R.1 Q.1 Maximum Subarray Sum.
`You are given an array 'arr' of length 'n', consisting of integers.`
`A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.`
`Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.`
`The sum of an empty subarray is 0.`
# https://leetcode.com/problems/maximum-subarray/description/
```py
def maxSubArray(self, nums: List[int]) -> int:
    overall_max = nums[0]
    curr_max = nums[0]

    for num in nums[1:]:
        curr_max = max(num, num+curr_max)
        overall_max = max(overall_max, curr_max)
    
    return overall_max
```

Q.2 Connect n ropes with minimum cost.
`You have been given 'N' ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.`
`The test-data is such that the result will fit into a 32-bit integer.`
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
```py
def connectRopes(heap: List[int]) -> int:
    heapq.heapify(heap)
    ans = 0
    
    while len(heap) > 1:
        one, two = heapq.heappop(heap), heapq.heappop(heap)
        ans = ans + one + two
        heapq.heappush(heap, one+two)
    
    return ans
```
Q. 3. Left View of Binary Tree
`You have been given a Binary Tree of 'n' nodes, where the nodes have integer values Print the left view of the binary tree.`
```py
def leftView(root: Optional[TreeNode]) -> List[int]:
    ans = []
    if root:
        q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if i == 0:
                ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return ans
```

R.2 Q. 1. Triplets in Binary Tree.
`You have been given a Binary Tree of integers and an integer 'X'. Find all the triplets in the tree whose sum is strictly greater than 'X'. The nodes in the triplet must hold the relationship of grandparent-parent-child.`
```py
def getTriplets(root: Optional[TreeNode], x) -> List[List[int]]:
    ans = []
    def preOrder(node: Optional[TreeNode], parent: Optional[TreeNode], gparent: Optional[TreeNode]) -> None:
        if parent and gparent and node.val + parent.val + gparent.val > x:
            ans.append([node.val, parent.val, gparent.val])
        if node.left:
            preOrder(node.left, node, parent)
        if node.right:
            preOrder(node.right, node, parent)
    
    preOrder(root, None, None)
    return ans
```

Q.2 Loot Houses.
`A thief wants to loot houses. He knows the amount of money in each house. He cannot loot two consecutive houses. Find the maximum amount of money he can loot.`
# https://leetcode.com/problems/house-robber/description/
```py
def rob(self, nums: List[int]) -> int:
    N = len(nums)
    dp = [0] * (N + 2)
    for i in range(N-1, -1, -1):
        dp[i] = max(dp[i+1], dp[i+2]+nums[i])
    
    return dp[0]
```