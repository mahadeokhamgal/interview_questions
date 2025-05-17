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