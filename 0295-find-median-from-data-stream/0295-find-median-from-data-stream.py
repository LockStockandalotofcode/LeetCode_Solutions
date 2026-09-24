import heapq

class MedianFinder:

    def __init__(self):
        self.lower_heap = []
        self.upper_heap = []
        # self.lower_half_max = self.lower_heap[0]
        # self.upper_half_min = self.upper_heap[0]

    def addNum(self, num: int) -> None:
        if len(self.lower_heap) == 0:
            heapq.heappush(self.lower_heap, -num)
        elif num <= ( - self.lower_heap[0]):
            heapq.heappush(self.lower_heap, -num)
        elif num >= ( - self.lower_heap[0]):
            heapq.heappush(self.upper_heap, num)
        
        if self._size_diff_invalid():
            self._balance_heaps()

    def _size_diff_invalid(self) -> bool:
        if not 0 <= (len(self.lower_heap) - len(self.upper_heap)) <= 1:
            return True
        return False

    def _balance_heaps(self) -> None:
        if len(self.lower_heap) > len(self.upper_heap):
            heapq.heappush(self.upper_heap, - heapq.heappop(self.lower_heap))
        elif len(self.lower_heap) < len(self.upper_heap):
            heapq.heappush(self.lower_heap, - heapq.heappop(self.upper_heap))
        return

    def findMedian(self) -> float:
        size_stream = len(self.lower_heap) + len(self.upper_heap)
        if size_stream % 2 == 0:
            return (-self.lower_heap[0] + self.upper_heap[0]) / 2

        return (- self.lower_heap[0])

        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()