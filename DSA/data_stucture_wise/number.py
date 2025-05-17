import math

def getReverse(num: int) -> int:
    ans = 0
    while num > 0:
        ans = (ans*10) +( num % 10)
        num = math.floor(num /10)

    return ans

# print(getReverse(12345))

def numberOfWays(n):
    if n < 0: return 0
    elif n == 0: return 1
    else: return numberOfWays(n - 1) + numberOfWays(n - 2)

print(numberOfWays(4))