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