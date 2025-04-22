"""Q1. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""
from typing import List
import collections

def groupAnagrams(strs : List[str]) -> List[List[str]]:
    map = collections.defaultdict(list)
    for str in strs:
        sortedStr = "".join(sorted(str))
        map[sortedStr].append(str)
    
    return map.values()

# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))