import heapq

class PriorityQueue:
    def __init__(self, map_data):
        self.heap = [(value, key) for key, value in map_data.items()]
        heapq.heapify(self.heap)

    def push(self, key, value):
        heapq.heappush(self.heap, (value, key))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")
        return self.heap[0][1]

    def size(self):
        return len(self.heap)

