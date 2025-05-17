# Microsoft - SDE-1
**https://www.naukri.com/code360/interview-experiences/microsoft/microsoft-interview-experience-by-off-campus-feb-2021-1000?testVariant=0**

R1. Q1. Buying And Selling Stock.
`You have been given the prices of 'N' stocks in an array where each array element represents the stock price for that day. You need to find the maximum profit which you can make by buying and selling the stocks. You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.`
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
```py
def maxProfit(self, prices: List[int]) -> int:
    N = len(prices)
    profit = 0
    buyPrice = float('inf')
    for price in prices:
        if price > buyPrice:
            profit += price - buyPrice
        buyPrice = price
                
    return profit
```

R.2 Q.1 Time to Burn Tree
`You have a binary tree of 'N' unique nodes and a Start node from where the tree will start to burn. Given that the Start node will always exist in the tree, your task is to print the time (in minutes) that it will take to burn the whole tree.`
`It is given that it takes 1 minute for the fire to travel from the burning node to its adjacent node and burn down the adjacent node.`
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
```py
def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    graph = defaultdict(list)
    def createGraph(node: Optional[TreeNode]) -> None:
        nonlocal graph
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            createGraph(node.left)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            createGraph(node.right)
    
    createGraph(root)
    
def getMinimumTimeForGraph(adjList, startL) -> int:
    time = -1
    q = deque([startL])
    seen = set([startL])
    while q:
        time += 1
        for i in range(len(q)):
            node = q.popleft()
            for adj in adjList[node]:
                if adj not in seen:
                    q.append(adj)
                    seen.add(adj)
    
    return time
return getMinimumTimeForGraph(graph, start)
```

R.3 Q. 1. Flatten Binary Tree.
`You are given a binary tree consisting of 'n' nodes.`
`Convert the given binary tree into a linked list where the linked list nodes follow the same order as the pre-order traversal of the given binary tree.`
`Use the right pointer of the binary tree as the “next” pointer for the linked list and set the left pointer to NULL`
`Use these nodes only. Do not create extra nodes.`
# Leetcode 114 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
```py
def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return None
    
    leftTail = self.flatten(root.left)
    rightTail = self.flatten(root.right)

    if root.left:
        leftTail.right = root.right
        root.right = root.left
        root.left = None
    
    return rightTail or leftTail or root
```

R.4 Q.1 Gray Code.
`Given a number ‘grayNumber’. Find the gray code sequence.`
Conditions for a gray code sequence :
1. Gray code sequence contains numbers from 0 to 2^'grayNumber'-1 in bit/binary form.
2. Two consecutive gray code sequence numbers only differ by 1 bit.
3. Gray code sequence must start with 0.
# https://leetcode.com/problems/gray-code/description/
```py
def grayCode(self, n: int) -> List[int]:
    ans = [0]
    seen = set([0])

    for _ in range(1 << n):
        for x in range(n):
            newNum = (1 << x) ^ ans[-1]
            if newNum not in seen:
                ans.append(newNum)
                seen.add(newNum)
                break

    return ans
```