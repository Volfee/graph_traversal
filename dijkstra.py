import queue
from priority_queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

import graph

class DijkstraAlgorithm:
	"""
	>>> dijkstra = DijkstraAlgorithm()
	>>> dijkstra.run(my_graph, 1, 3)
	"""

	def __init__(self):
		self.shortest_path = []
		self.total_weight = 0

	# @dataclass(order=True)
	# class PrioritizedNode():
	# 	item: Any=field(compare=False)
	# 	priority: int
		

	def run(self, graph, start) -> None:
		fringe = PriorityQueue()
		distances = {node: float('inf') for node in graph.getNodes()}
		self.edge_to = {node: None for node in graph.getNodes()}
		visited = set()

		for node, priority in distances.items():
			fringe.add(node, priority)

		# Change priority of starting element.
		fringe.change_priority(start, new_priority=0)
		distances[start] = 0

		current_node = None
		while fringe.empty():
			current_node, current_dist = fringe.get()
			# Add node to visited.
			visited.add(current_node)

			print(f"Current: {current_node, current_dist}, {fringe}")

			# Add neighbours to priority queue.
			neighbours = graph.get_neighbours(current_node)
			for neighbour in neighbours:
				if neighbour not in visited:
					weight = graph.get_weight(current_node, neighbour) + current_dist
					if (distances[neighbour] > weight):
						print(f"Priority changed {neighbour}, {distances[neighbour]} => {weight}")
						distances[neighbour] = weight
						fringe.change_priority(neighbour, new_priority=weight)
						self.edge_to[neighbour] = current_node 

		print("Finished.")

	def get_shortest_path(self, to):
		path = []
		while to:
			path.append(to)
			to = self.edge_to[to]
		return path[::-1]




test_graph = graph.Graph()
test_graph.add_node("A")
test_graph.add_node("B")
test_graph.add_node("C")
test_graph.add_node("D")
test_graph.add_node("F")

test_graph.add_edge("A", "B", 3)
test_graph.add_edge("A", "C", 1)
test_graph.add_edge("B", "C", 1)
test_graph.add_edge("B", "D", 1)
test_graph.add_edge("C", "D", 3)
test_graph.add_edge("B", "F", 7)


dijkstra = DijkstraAlgorithm()
dijkstra.run(test_graph, "F")		
print(dijkstra.get_shortest_path(to="C"))
		



