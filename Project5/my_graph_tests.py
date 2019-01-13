#my_graph_tests.py
import unittest
from my_graph import *

class Test_My_Graph(unittest.TestCase):

   def test_bicolor(self):
      pass


graph1 = MyGraph("graph1.txt")
connections = graph1.conn_components()
print(connections)
print(graph1.bicolor())

#graph2 = MyGraph("graph2.txt")
#connections2 = graph2.conn_components()
#print(connections2)
#print(graph2.bicolor())

if __name__ == '__main__':
   unittest.main()