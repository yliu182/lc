"""
155. Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
    Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
           [[],[-2],[0],[-3],[],[],[],[]]
    Output: [null,null,null,null,-3,null,0,-2]

Constraints:
    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""



""""
Yao 写的第一个版本，错误的理解成了 minHeap

class MinStack:

    def __init__(self):
        self.heap = []


    def push(self, val: int) -> None:
        # append the new element to the end, and sift_up
        self.heap.append(val)
        i = len(self.heap) - 1

        while True:
            parent = (i-1) // 2
            if parent < 0 or self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def pop(self) -> None:
        # swap heap[0] with heap[last], and do sift_down
        size = len(self.heap)
        self.heap[0], self.heap[size-1] = self.heap[size-1], self.heap[0]
        self.heap.pop()
        i = 0
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


    def top(self) -> int:
        return self.heap[0]

    def getMin(self) -> int:
        return self.heap[0]

"""


class MinStack:
    def __init__(self):
        # each element is a tuple(val, smallest val so far)
        self.heap = []

    def push(self, val: int) -> None:
        if len(self.heap) == 0:
            self.heap.append((val, val))
            return
        smallest = self.heap[-1][1]
        smallest = min(smallest, val)
        self.heap.append((val, smallest))

    def pop(self) -> None:
        self.heap.pop()

    def top(self) -> int:
        return self.heap[-1][0]


    def getMin(self) -> int:
        return self.heap[-1][1]
