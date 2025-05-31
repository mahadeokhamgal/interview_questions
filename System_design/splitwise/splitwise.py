import collections
from typing import List
import heapq

def get_spliwise_pay(expences: List) -> List[str]:
    userwise = collections.defaultdict(int)
    for user, amt in expences:
        userwise[user] += amt

    debters = []
    creditors = []
    
    for user, amt in userwise.items():
        if amt < 0:
            heapq.heappush(debters, (amt, user))
        elif amt > 0:
            heapq.heappush(creditors, (-amt, user))
    
    owe_list = []
    while debters and creditors:
        debt_amount, max_debter = heapq.heappop(debters)
        credit_amt, max_crediter = heapq.heappop(creditors)

        debt_amount = abs(debt_amount)
        credit_amt = abs(credit_amt)

        settlement_amt = min(credit_amt, debt_amount)
        delta = max(credit_amt, debt_amount) - settlement_amt

        if credit_amt > debt_amount:
            heapq.heappush(creditors, (-delta, max_crediter))
        elif credit_amt < debt_amount:
            heapq.heappush(debters, (-delta, max_debter))

        owe_list.append(f'{max_debter} ows {settlement_amt} to {max_crediter}')

    return owe_list

    """
    {
    'Alice': -425, : 0  = Alice owes 425 to David
    'Bob': -50, : 0 = Bob owes 50 to David
    'Charlie': -50, : 0 = Charlie owes 50 to David
    'David': 2450, : 525 : 100 : 50 : 0
    'Mark': -1925, : 0  = Mark owes 1925 to David
    }
    """

    return []

tc1 = [
    ["Alice", 250],
    ["Alice", -50],
    ["Bob", -50],
    ["Charlie", -50],
    ["David", -50],
    ["Mark", -50],
    ["Alice", 750],
    ["Mark", -250],
    ["David", -250],
    ["Mark", -250],
    ["David", 2750],
    ["Alice", -1375],
    ["Mark", -1375],
]
print(get_spliwise_pay(tc1))