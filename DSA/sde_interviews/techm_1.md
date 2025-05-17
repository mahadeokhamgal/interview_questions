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