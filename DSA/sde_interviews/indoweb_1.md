
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