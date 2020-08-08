import collections

class Graph:
	"""
	Directed and weighted graph using adjacency list
	"""

	def __init__(self):
		self.adjacency_list = dict()

	def add_node(self, value):
		node = self.GraphNode(value)
		self.adjacency_list[value] = node

	def add_edge(self, val1, val2, weight, directional=False):
		"""
		Creates edge from node with val1 and node with val2 with given weight.
		"""
		node1 = self.get_node(val1)
		node2 = self.get_node(val2)

		node1.add_edge(node2, weight)
		if not directional:
			node2.add_edge(node1, weight)

	def get_node(self, value):
		return self.adjacency_list[value]

	def has_edge(self, val1, val2):
		"""
		Checks if there is an edge from node with val1 to node with val2.
		"""
		node1 = self.get_node(val1)
		node2 = self.get_node(val2)

		return node1.has_edge(node2)

	def get_weight(self, val1, val2):
		"""
		Returns weight of edge from node with val1 to node with val2.
		"""

		node1 = self.get_node(val1)
		node2 = self.get_node(val2)

		return node1.get_weight(node2)

	def getNodes(self):
		return set(self.adjacency_list.values())

	def __repr__(self):
		return "Graph()"

	def __str__(self):
		size = len(self.adjacency_list)
		representation = f"Graph - {size} nodes:\n"

		for node in self.adjacency_list.values():
			representation += str(node) + "\n"

		return representation



	class GraphNode:
		"""
		Building block 
		"""

		def __init__(self, value):
			self.value = value
			self.edges = dict()

		def __eq__(self, otherNode):
			return otherNode.value == self.value

		def __hash__(self):
			return hash(self.value)

		def has_edge(self, otherNode):
			"""
			Checks if node is adjacent to this node.
			"""
			return otherNode in self.edges

		def add_edge(self, otherNode, weight):
			self.edges[otherNode] = weight

		def get_weight(self, edge_to):
			return self.edges[edge_to]
			

		def __repr__(self):
			return f"Node({self.value})"

		def __str__(self):
			return f"Node({self.value}): [{self.edges}]"
