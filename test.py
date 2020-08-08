import unittest
import graph

class GraphTest(unittest.TestCase):

	def testIntegration(self):
		test_graph = graph.Graph()
		test_graph.add_node(1)
		test_graph.add_node(2)
		test_graph.add_edge(1,2,2)

	def testHasConnection(self):
		test_graph = graph.Graph()
		test_graph.add_node(1)
		test_graph.add_node(2)
		test_graph.add_node(3)
		test_graph.add_edge(1,2,2)
		test_graph.add_edge(2,3,2)

		self.assertTrue(test_graph.has_edge(1,2))
		self.assertFalse(test_graph.has_edge(1,3))

	def testHasConnectionDirection(self):
		test_graph = graph.Graph()
		test_graph.add_node(1)
		test_graph.add_node(2)
		test_graph.add_node(3)
		
		test_graph.add_edge(1, 2, 2, directional=True)
		self.assertTrue(test_graph.has_edge(1,2))
		self.assertFalse(test_graph.has_edge(2,1))

		test_graph.add_edge(2, 3, 2)
		self.assertTrue(test_graph.has_edge(2,3))
		self.assertTrue(test_graph.has_edge(3,2))

	def testgetWeight(self):
		test_graph = graph.Graph()
		test_graph.add_node(1)
		test_graph.add_node(2)
		test_graph.add_edge(1,2,4)

		self.assertEqual(test_graph.get_weight(1,2), 4)

if __name__ == '__main__':
	unittest.main()