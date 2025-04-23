
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
