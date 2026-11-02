"""
399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent the equation
Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Example 1:
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
           queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.0, 0.5, -1.0, 1.0, -1.0]

Example 2:
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
           queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75, 0.4, 5.0, 0.2]

Example 3:
    Input: equations = [["a","b"]], values = [0.5],
           queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.5, 2.0, -1.0, -1.0]

Constraints:
    - 1 <= equations.length <= 20
    - equations[i].length == 2
    - 1 <= Ai.length, Bi.length <= 5
    - values.length == equations.length
    - 0.0 < values[i] <= 20.0
    - 1 <= queries.length <= 20
    - queries[j].length == 2
"""

from typing import List

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for equation, value in list(zip(equations, values)):
            start = equation[0]
            end = equation[1]
            graph[start].append((end, value))
            # 必须是双向图
            graph[end].append((start, 1.0 / value))

        def calculate(begin: str, end: str) -> float:
            if begin not in graph or end not in graph:
                return -1.0
            if begin == end:
                return 1.0
            visited = set()

            def dfs(node: str, product: float) -> float:
                if node == end:
                    return product
                visited.add(node)

                ans = float('-inf')
                for node_next, val in graph[node]:
                    if node_next in visited:
                        continue

                    result = dfs(node_next, val * product)
                    if result != -1.0:
                        return result
                return -1.0

            return dfs(begin, 1.0)

        return [calculate(q[0], q[1]) for q in queries]
