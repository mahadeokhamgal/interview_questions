from typing import List
from collections import defaultdict

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

print(allPaths([[1, 2, 3],[4, 5, 6]]))

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

# print(sort_zeros_n_ones([1,0,1,0,1,1,0,0,1,0]))

# LeetCode 209: Minimum Size Subarray Sum
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

# print(minSubArray([1, 2, 3, 4, 5], 11))

def subarrayWithSum(nums: List[int], k: int) -> List[int]:
    """Brute force
    for i in range(len(nums)-1):
        currSum = nums[i]
        for j in range(i+1, len(nums)):
            currSum += nums[j]
            if currSum == k:
                return [i, j]
    
    return [-1, -1]
    """
    """Optimised"""
    
    prefixSum = 0
    preFixSumMap = {0: -1}

    for idx, num in enumerate(nums):
        prefixSum += num

        if (prefixSum - k) in preFixSumMap:
            return [preFixSumMap[prefixSum-k]+1, idx]
        if prefixSum not in preFixSumMap:
            preFixSumMap[prefixSum] = idx
            
    return [-1, -1]

# print(subarrayWithSum([1,2,3,4], 7))
    # IP - [1,2,3,4], 7, OP - [2, 3]
