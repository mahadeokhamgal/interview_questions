#`An array ‘A’ of ‘N’ integers is provided. Return the maximum possible number which can be created by taking bitwise XOR of any 2 integers of the array.`
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
    

# print(getMaxXor([1, 2, 3, 7, 9])) # 14
# print(getMaxXor([7, 7, 7, 7])) # 0
# print(getMaxXor([1, 2, 4, 8])) # 12
# print(getMaxXor([1023, 512, 2048, 4096])) # 6144
print(getMaxXor([3,10,5,25,2,8]))