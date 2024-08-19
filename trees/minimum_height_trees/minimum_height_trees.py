from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        nodes_graph = {}
        for u, v in edges:
            nodes_graph[u] = nodes_graph.get(u, [])
            nodes_graph[u].append(v)
            nodes_graph[v] = nodes_graph.get(v, [])
            nodes_graph[v].append(u)
        leaves = [leaf for leaf in range(n) if len(nodes_graph[leaf]) <= 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = nodes_graph[i].pop()
                nodes_graph[j].remove(i)
                if len(nodes_graph[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves



if __name__ == "__main__":
    graph = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,7],[1,8],[1,9]]
    n = 10
    sol = Solution()
    print(sol.findMinHeightTrees(n, graph))