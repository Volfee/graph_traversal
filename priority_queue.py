import heapq
from dataclasses import dataclass, field
from typing import Any

class PriorityQueue:


	def __init__(self):
		self.heap = list()

	def add(self, item, priority):
		heapq.heappush(self.heap, self.pItem(priority, item)) 

	def get(self):
		item = heapq.heappop(self.heap)
		return item.value, item.priority

	def change_priority(self, item, new_priority):
		# find item
		for heap_item in self.heap:
			if heap_item.value == item:
				heap_item.priority = new_priority

		heapq.heapify(self.heap)

	def empty(self):
		return bool(self.heap)

	def __str__(self):
		result = "PriorityQueue("
		copy = self.heap.copy()

		while(copy):
			result += str(heapq.heappop(copy)) + ", "

		return result + ")"

	@dataclass(order=True)
	class pItem:
		"""Wrapper for item to store priority."""
		priority: int
		value: Any = field(compare=False)

		def __str__(self):
			return f"({self.value}, {self.priority})"


if __name__ == '__main__':
	pq = PriorityQueue()
	print(pq)
	pq.add("car", 1)
	print(pq)
	pq.add("gar", 4)
	print(pq)
	pq.add("var", 2)
	print(pq)

	pq.change_priority("car", 5)
	print(pq)