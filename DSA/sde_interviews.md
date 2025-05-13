
**Tech M interview - https://www.naukri.com/code360/interview-experiences/tech-mahindra/tech-mahindra-interview-experience-senior-software-engineer-sep-2021-exp-0-2-years-2098?cvId=c285d94fb9f24628ac418c8dcea08985&campaign=interview_exp_dashboard&medium=desktop&source=naukri**
`R1 Q.1 You are given a Singly Linked List of integers which is sorted based on absolute value.`
`You have to sort the Linked List based on actual values.`
`The absolute value of a real number x, denoted |x|, is the non-negative value of x without regard to its sign.`
`Example: If the given list is {1 -> -2 -> 3} (which is sorted on absolute value), the returned list should be {-2 -> 1 -> 3}.`
 1. Bruteforce - Bubble sort.
 ```py
 def bubbleSort(self) -> Node:
    if not (self.head and self.head.next):
        return self.head
    
    swapped = True
    while swapped:
        swapped = False
        temp = self.head
        while temp and temp.next:
            if temp.val > temp.next.val:
                localTemp = temp.val
                temp.val = temp.next.val
                temp.next.val = localTemp
                swapped = True
            temp = temp.next
    
    return self.head
```

 2. optimal approach. sort_from_absolute.
 ```py
    def sort_from_absolute(self) -> Node:
        temp = self.head
        while temp and temp.next:
            if temp.next.val < 0:
                to_move = temp.next
                temp.next = to_move.next
                to_move.next = self.head
                self.head = to_move
            else:
                temp = temp.next

        return self.head
```

`R2. Q2. You are given an array consisting of 'N' positive integers where each integer is either 0 or 1 or 2.`
`Your task is to sort the given array in non-decreasing order.`
```py
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
```

**https://www.naukri.com/code360/interview-experiences/ltimindtree/interview-experience-by-priyanshu-agarwal-on-campus-feb-2025**
**ltimindtree**
R1. Q1.
Which of these is not a pillar of OOPS?
(A) Encapsulation
(B) Polymorphism
(C) Abstraction
(D) Compilation
(E) Inheritance
- Compilation
R1. Q2.
`Write function to find reverse of a number.`
```py
def getReverse(num: int) -> int:
    ans = 0
    while num > 0:
        ans = (ans*10) +( num % 10)
        num = math.floor(num /10)

    return ans
```
R1. Q3.
`An array ‘A’ of ‘N’ integers is provided. Return the maximum possible number which can be created by taking bitwise XOR of any 2 integers of the array.` - **LeetCode Problem 421**
```py
class Node:
    def __init__(self):
        self.zero: Node = None
        self.one: Node = None
    
class Trie:
    def __init__(self):
        self.root = Node()

    def addNum(self, num: int) -> None:
        temp = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 1:
                if not temp.one:
                    temp.one = Node()
                temp = temp.one
            else:
                if not temp.zero:
                    temp.zero = Node()
                temp = temp.zero

    def getMaxXorFor(self, num: int) -> int:
        bestXor = 0
        temp = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            reqBit = 1 if bit == 0 else 0
            if (reqBit == 1 and temp.one) or (reqBit == 0 and temp.zero):
                bestXor = bestXor << 1 | 1 # we got the required bit, so we add 1 to right.
                temp = temp.one if reqBit == 1 else temp.zero
            else:
                bestXor = bestXor << 1
                temp = temp.one if bit == 1 else temp.zero
        
        return bestXor
            

def getMaxXor(nums: list) -> int:
    trie = Trie()

    for num in nums:
        trie.addNum(num)

    return max(trie.getMaxXorFor(num) for num in nums)
    """
    Brute Force
    ans = float('-infinity')
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            ans = max(ans, nums[i]^nums[j])
            if nums[i]^nums[j] == 28:
                print(nums[i], nums[j])
    for num in nums:
        print(bin(num))
    return ans
    """
```

R2. Q1.
`Given an array/list 'ARR' of integers and an integer ‘K’. You are supposed to return the length of the shortest subarray that has a sum greater than or equal to ‘K’. If there is no subarray with a sum greater than or equal to K, then return -1.`
`Note :`
`An array ‘B’ is a subarray of an array ‘A’ if ‘B’ that can be obtained by deletion of, several elements(possibly none) from the start of ‘A’ and several elements(possibly none) from the end of ‘A’.`
**LeetCode 209: Minimum Size Subarray Sum**
```py
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
```

R2. Q2. **Leetcode 525: **
`You are given an array consisting of 0s and 1s. You need to find the length of the largest subarray with an equal number of 0s and 1s.`
```py
def findMaxLength(nums: List[int]) -> int:
    # brute force = time - n^2, space - 1
    N = len(nums)
    best = 0
    for i in range(N-1):
        freq = [0, 0]
        freq[nums[i]] += 1
        for j in range(i+1, N):
            freq[nums[j]] += 1
            if freq[0] == freq[1]:
                best = max(best, j-i+1)
    
    return best
    
    # optimised   = time - n, space - n
    best = 0
    counts = [0, 0]
    hashMap = defaultdict(int)
    hashMap[0] = -1
    for idx in range(len(nums)):
        counts[nums[idx]] += 1
        currDiff = counts[1] - counts[0]
        if currDiff in hashMap:
            best = max(best, idx-hashMap[currDiff])
        if currDiff not in hashMap:
            hashMap[currDiff] = idx
    
    return best
```

**Oracle**
**https://www.naukri.com/code360/interview-experiences/oracle/oracle-interview-experience-senior-software-engineer-mar-2022-exp-0-2-years**

R1. Q1. Subarray With Given Sum **Leetcode: 560: Subarray Sum Equals K**
`Given an array ARR of N integers and an integer S. The task is to find whether there exists a subarray(positive length)`
` of the given array such that the sum of elements of the subarray equals to S or not. If any subarray is found,`
`return the start and end index (0 based index) of the subarray. Otherwise, consider both the START and END indexes as -1.`
`Note: If two or more such subarrays exist, return any subarray.`
`For Example: If the given array is [1,2,3,4] and the value of S is equal to 7. Then there are two possible subarrays having sums`
` equal to S are [1,2,3] and [3,4].`
```py
def subarrayWithSum(nums: List[int], k: int) -> List[int]:
    """Brute force
    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            if currSum == k:
                return [i, j]
    
    return [-1, -1]
    """
    """Optimal"""
    prefixSum = 0
    preFixSumMap = {0: -1}

    for idx, num in enumerate(nums):
        prefixSum += num

        if (prefixSum - k) in preFixSumMap:
            return [preFixSumMap[prefixSum-k]+1, idx]
        if prefixSum not in preFixSumMap:
            preFixSumMap[prefixSum] = idx
            
    return [-1, -1]
```

R1. Q2.
`You are given a Singly Linked List of integers and an integer array 'B' of size 'N'. Each element in the array 'B' represents a block size. Modify the linked list by reversing the nodes in each block whose sizes are given by the array 'B'.`
Linked list: 1->2->3->4->5
Array B: 3 3 5
Output: 3->2->1->5->4
**To do** this question solution.

**Indo Web Agency Pvt. Ltd. SDE-1**
**https://www.naukri.com/code360/interview-experiences/indo-web-agency-pvt-ltd/interview-experience-off-campus-feb-2025**
`Round 1`
Q.1 - Puzzle
You have two eggs and a 100-story building. You need to figure out the highest floor from which you can drop an egg without it breaking. You are allowed to drop the eggs only once from each floor, and the eggs are identical.
What is the minimum number of drops required to find the highest floor from which you can drop an egg without it breaking?
`Ans - `
**Wrong**
- The answere is to use `Binary Search algorithm` to solve this.
- call lowesr floor from which egg will not break = `Target floor`.
- Start by finding the middle floor of the building i.e. e.g. 0 + (100-0)//2 = 50, and drop the egg and check if it breaks.
- If the egg breaks that means that Target floor is in range(0, 49) (low, mid-1). else if egg did not break means target floor is in range 50 to 100 (mid to high).
- This way we can get the number of minimum eggs needed by formula as log n (n is number of floors and log is base 2 as every operation halves the input).
- so the ans is log(100) = 6.6438 = 7
**Correct**
- To solve the 2-egg, 100-floor egg drop puzzle optimally, binary search is not the best approach due to the constraint of only having two eggs.
- Instead, we use a strategy that minimizes the worst-case number of drops. The idea is to drop the first egg from floors in decreasing intervals: first from floor 14, then 13 floors higher (floor 27), then 12 floors higher (floor 39), and so on. This way, in the worst-case scenario (the egg breaks late), you still only need 14 drops.

Mathematically, we solve for the smallest integer x such that:
```py
    x(x+1)/2 ≥ 100
```
Solving this, x = 14. So, the minimum number of drops in the worst case is 14.

`Round - 2`
Q.1 - Find the number of duplicate digits in the given integer which is taken as input.

2376. Count Special Integers.
```py
def countSpecialNumbers(n: int) -> int:
    digits = list(map(int, str(n)))
    @cache
    def dp(ptr, mask, is_tight, is_num):
        if ptr == len(digits):
            return int(is_num) # this will return 1 if is_num is true else 0.
        
        ans = 0
        if not is_num:
            ans += dp(ptr+1, mask, False, False)
        lowerBound = 0 if is_num else 1
        upperBound = digits[ptr] if is_tight else 9
        for d in range(lowerBound, upperBound+1):
            if not mask >> d & 1:
                ans += dp(ptr + 1, mask | 1 << d, is_tight and (d == upperBound), True)
        
        return ans
    return dp(0, 0, True, False)
```

1012. Numbers With Repeated Digits.
```py
def numDupDigitsAtMostN(self, N: int) -> int:
    """Brute Force
    def isRepeated(num: int) -> bool:
        seen = [False] * 10
        while num:
            digit = num % 10
            if seen[digit]:
                return True
            seen[digit] = True
            num //= 10
        return False
    ans = 0
    for i in range(1, N+1):
        if isRepeated(i):
            ans += 1
    
    return ans
    """

    def countSpecialNumbers(n: int) -> int:
        digits = list(map(int, str(n)))
        @cache
        def dp(ptr, mask, is_tight, is_num):
            if ptr == len(digits):
                return int(is_num) # this will return 1 if is_num is true else 0.
            ans = 0
            if not is_num:
                ans += dp(ptr+1, mask, False, False)
            lowerBound = 0 if is_num else 1
            upperBound = digits[ptr] if is_tight else 9
            for d in range(lowerBound, upperBound+1):
                if not mask >> d & 1:
                    ans += dp(ptr + 1, mask | 1 << d, is_tight and (d == upperBound), True)
            return ans
        return dp(0, 0, True, False)
    return N - countSpecialNumbers(N)
```

Q2. `Merge k sorted lists.`
- You are given an array of k sorted linked lists. Merge all the linked lists into one sorted linked list and return it.
```py
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummyNode = ListNode(0)
    currNode = dummyNode
    while heap:
        val, i, node = heapq.heappop(heap)
        currNode.next = node
        currNode = currNode.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
        
    return dummyNode.next
```

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

**amazon SDE-1**
**https://www.naukri.com/code360/interview-experiences/amazon/amazon-interview-experience-by-amrith-m-nair-on-campus-jan-2019-21?testVariant=0**
1. Tiling Problem.
`Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile.`
- Input n = 3
- Output: 3
Explanation:
We need 3 tiles to tile the board of size  2 x 3.  
We can tile the board using following ways
1) Place all 3 tiles vertically.  
2) Place first tile vertically and remaining 2 tiles horizontally.
3) Place first 2 tiles horizontally and remaining tiles vertically.
GFG - **https://www.geeksforgeeks.org/tiling-problem/**

```py
def numberOfWays(n):
    if n < 0: return 0
    elif n == 0: return 1
    else: return numberOfWays(n - 1) + numberOfWays(n - 2)
```

2. Find k’th character of decrypted string.
`Given an encoded string where repetitions of substrings are represented as substring followed by count of substrings. For example, if encrypted string is “ab2cd2” and k=4 , so output will be ‘b’ because decrypted string is “ababcdcd” and 4th character is ‘b’.`
`Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times. No leading 0 is present in frequency of substring.`
Input: "a2b2c3", k = 5
Output: c
Decrypted string is "aabbccc"
Leetcode # 880 **https://leetcode.com/problems/decoded-string-at-index/**
```py
def decodeAtIndex(self, s: str, k: int) -> str:
    size = 0
    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1

    for char in reversed(s):
        k %= size
        if k == 0 and char.isalpha():
            return char
        if char.isdigit():
            size //= int(char)
        else:
            size -= 1
```

R.2
Q.1 `Count Positive-Negative Pairs`
Given an array of positive and negative integers, print x if +x and -x are present in the array.
**https://www.geeksforgeeks.org/problems/positive-negative-pair5209/1**
- returns a list of integers denoting the pairs. The pair that appears first(i.e. second element of the pair appears first) in A[] should appear first in the returning list and within the pair, the negative integer should appear before the positive integer. Return an empty integer list if no such pair exists.
IP = [1,3,6,-2,-1,-3,2,7]
Output: -1 1 -3 3 -2 2
```py
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
```

Q.2 Design the logic for minimising cash flow in an app like ‘Splitwise’.
RAW IP = expenses = [
    {"payer": "Alice", "amount": 90, "participants": ["Alice", "Bob", "Charlie"]},
    {"payer": "Bob", "amount": 60, "participants": ["Bob", "David", "Eve"]},
    {"payer": "Charlie", "amount": 50, "participants": ["Alice", "Bob", "Charlie", "David", "Eve"]}
]

`IP` = {
    "Alice": -70,
    "Bob": 50,
    "Charlie": -30,
    "David": 60,
    "Eve": -10
}
OP = `['Alice pays 60.00 to David', 'Charlie pays 30.00 to Bob', 'Alice pays 10.00 to Bob', 'Eve pays 10.00 to Bob']`

```py
def build_balances(expenses):
    balances = {}

    for expense in expenses:
        payer = expense['payer']
        amount = expense['amount']
        participants = expense['participants']

        share = amount / len(participants)

        # Initialize balances
        for person in participants + [payer]:
            balances.setdefault(person, 0)

        for person in participants:
            balances[person] -= share  # each participant owes their share
        balances[payer] += amount     # payer gets full credit

    return balances

def minimize_cash_flow(balances: dict):
    transactions = []

    def get_max_creditor():
        return max(balances, key=lambda x: balances[x])

    def get_max_debtor():
        return min(balances, key=lambda x: balances[x])

    while True:
        max_creditor = get_max_creditor()
        max_debtor = get_max_debtor()

        credit = balances[max_creditor]
        debt = balances[max_debtor]

        if abs(credit) < 1e-9 and abs(debt) < 1e-9:
            break  # All settled

        amount = min(credit, -debt)
        balances[max_creditor] -= amount
        balances[max_debtor] += amount

        transactions.append(f"{max_debtor} pays {amount:.2f} to {max_creditor}")

    return transactions
```

R3. 
1. **Count Special Nodes in Generic Tree**
`Given a generic tree, find the count of all special nodes. A node is a special node if there is a path from root to that node with all distinct elements. The input was not a pointer to a tree. He’d give me an adjacency list and an array of values where the value of ith node in the adjacency list is the ith element in the values array. He asked me not a create a tree out of the given information and rather do it with the adjacency list itself.`
GFG - **https://www.geeksforgeeks.org/number-of-special-nodes-in-an-n-ary-tree**
IP = count_special_nodes([[1, 2], [3, 4], [], [], []], [1, 2, 3, 4, 5])
OP = 5(All nodes are special)

        1 (0)
       /     \
   2 (1)     3 (2)
   /   \
4 (3) 5 (4)

```py
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

print(count_special_nodes([[1, 2], [3, 4], [], [], []], [1, 2, 3, 4, 5]))  
print(count_special_nodes([[1, 2], [3, 4], [], [], []], [1, 2, 1, 4, 2]))      
```

Q.2 **Common Digit Longest Subsequence**
`Given an integer array, find the longest subsequence with adjacent numbers having a digit in common. Eg: 1 12 44 29 33 96 89 . The longest subsequence here is { 1 12 29 96 89} and the answer is 5.`
GFG - **https://www.geeksforgeeks.org/longest-subsequence-such-that-adjacent-elements-have-at-least-one-common-digit**
IP = [1, 12, 44, 29, 33, 96, 89]
OP = [1, 12, 29, 96, 89].
# - a subsequence is derived by deleting zero or multiple elementd without changing the order.
```py
"""
Array: A collection of elements.
Subarray: A contiguous portion of the array.
Subsequence: A sequence that can be derived by removing elements without changing the order.
Prefix: A subarray starting from the first element.
Suffix: A subarray starting from any element but has to end at last element of array.
Increasing Subsequence: A subsequence where elements are in strictly increasing order.
Longest Increasing Subsequence (LIS): The longest strictly increasing subsequence.
Longest Common Subsequence (LCS): The longest subsequence common to two arrays.
Palindromic Subsequence: A subsequence that forms a palindrome.
"""
```
```py
# my approach is using dp, start from right and move to left, and try to maximise the subsequence from every idx in array.
# now find which subsequence is the longest.
def commonDigitLongestSubsequence(nums: List[int]) -> int:
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
    
    return ans
```

R.4. F2F
Q.1 `Given a binary tree, modify the tree satisfying the following constrains :`
`Value at root must be the sum of left child and right child (not subtrees). You can’t reduce the value at any node. You can only increase it. Value of root node must be minimum`

To Do.

Q.2 `Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order. You can scan the array only once.`
**https://leetcode.com/problems/sort-colors/**
```py
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        idx = 0
        right = len(nums) - 1

        while idx <= right:
            if nums[idx] == 0:
                nums[idx], nums[left] = nums[left], nums[idx]
                left += 1
                idx += 1
            elif nums[idx] == 2: 
                nums[idx], nums[right] = nums[right], nums[idx]
                right -= 1
            else:
                idx += 1
```
R.5
Q.1 `Difference between threads and processes.`
| Feature                 | **Process**                                                | **Thread**                                                             |
| ----------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Definition**          | Independent unit of execution with its own memory          | Lightweight unit within a process that shares memory                   |
| **Memory Space**        | Has its **own separate** memory space                      | Shares **common memory** with other threads in the same process        |
| **Communication**       | Slower and complex (requires **IPC**)                      | Faster and easier (uses **shared memory**)                             |
| **Creation Time**       | Slower to create and manage                                | Faster to create and switch between                                    |
| **Context Switching**   | Expensive, involves switching memory contexts              | Lightweight and faster                                                 |
| **Crash Impact**        | Crash is **isolated** to that process                      | Crash can **affect the entire process**                                |
| **Security/Isolation**  | Highly **isolated** from other processes                   | **Not isolated**, shared state may lead to issues like race conditions |
| **Use Cases**           | Used in **multitasking** (e.g., running multiple programs) | Used in **parallelism** within a single program (e.g., handling tasks) |
| **Resource Usage**      | More resource-heavy (needs more memory and setup)          | Lightweight and less resource-intensive                                |
| **Example in OS**       | Chrome runs each tab in a **separate process**             | A download manager uses **threads** for parallel file downloads        |
| **Programming Example** | Python: `multiprocessing.Process`                          | Python: `threading.Thread`                                             |

Q.2 `Deadlocks and its prevention.`
# Four Necessory conditions for deadlock.
| Condition            | Description                                                                        |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Mutual Exclusion** | At least one resource is held in a non-shareable mode                              |
| **Hold and Wait**    | A process is holding a resource and waiting for others                             |
| **No Preemption**    | Resources cannot be forcibly taken away                                            |
| **Circular Wait**    | A circular chain of processes exists, each waiting for a resource held by the next |

# Deadlock prevention.(Use any one of below).
| Strategy                       | How It Works                                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| **Eliminate Mutual Exclusion** | Make resources shareable (often impractical)                                                       |
| **Avoid Hold and Wait**        | Require processes to request all resources upfront                                                 |
| **Allow Preemption**           | If a resource is needed, forcibly take it from a lower-priority process                            |
| **Break Circular Wait**        | Impose an ordering on resource acquisition (e.g., always request resources in increasing ID order) |

Q.3 `Trie data structure.`
**Implement a Trie data structure and write functions to insert and search for a few words in it.**
```py
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        temp = self.root
        for char in word:
            temp = temp.children[char]
        temp.isEnd = True
    
    def isWord(self, word):
        temp = self.root
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.isEnd
```

Q.4. `Anagram Pairs.`
`Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.`
# https://leetcode.com/problems/valid-anagram/description/
```py
def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

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

SDE-1 Amazon
# https://www.naukri.com/code360/interview-experiences/amazon/amazon-interview-experience-by-anonymous-sde-1-dec-2020-exp-0-2-years-261?testVariant=0

R.1 Q.1 Maximum Subarray Sum.
`You are given an array 'arr' of length 'n', consisting of integers.`
`A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.`
`Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.`
`The sum of an empty subarray is 0.`
# https://leetcode.com/problems/maximum-subarray/description/
```py
```