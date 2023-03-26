class Node: 
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        return dfs(node)