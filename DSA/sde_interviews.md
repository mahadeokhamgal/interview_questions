
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
    # brute force = time - n^2
    # optimised   = time - n
    # 
    #  
```
**Oracle**
https://www.naukri.com/code360/interview-experiences/oracle/oracle-interview-experience-senior-software-engineer-mar-2022-exp-0-2-years?cvId=c285d94fb9f24628ac418c8dcea08985&campaign=interview_exp_dashboard&medium=desktop&source=naukri