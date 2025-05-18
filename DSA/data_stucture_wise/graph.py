import collections


def dfs_graph(edges):



    """BFS"""
    adjencyList = collections.defaultdict(list)
    for x, y in edges:
        adjencyList[x].append(y)
        adjencyList[y].append(x)
    
    print(adjencyList)
    seen = set()
    for node in adjencyList.keys():
        # print("first key", node)
        if node in seen:
            continue
        
        seen.add(node)
        print(node)
        for adj in adjencyList[node]:
            if adj not in seen:
                print(adj)
                seen.add(adj)
        
tc1 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D')
]
print(dfs_graph(tc1))