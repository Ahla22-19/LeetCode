class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adj_lst = defaultdict(list)
        outdegree = [0] * len(graph)

        for node, edges in enumerate(graph):
            outdegree[node] = len(edges)
            for edge in edges:
                adj_lst[edge].append(node)

        queue = deque()
        for node, outdeg in enumerate(outdegree):
            if outdeg == 0:
                queue.append(node)
        
        safeNode = [False for node in range(len(graph))]

        while queue:
            node = queue.popleft()
            safeNode[node] = True
            for nei in adj_lst[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    queue.append(nei)
        
        return [node for node, is_safe in enumerate(safeNode) if is_safe == True]

