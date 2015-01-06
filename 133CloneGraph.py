# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/clone-graph/

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        node_stack = []
        node_set = {}
        new_root = UndirectedGraphNode(node.label)
        node_set[new_root.label] = new_root
        node_stack.append(node)
        while len(node_stack)>0:
            current_node = node_stack.pop()
            current_new_node = node_set[current_node.label]
            for n in current_node.neighbors:
                if n.label in node_set.keys():
                    current_new_node.neighbors.append(node_set[n.label])
                else:
                    new_node = UndirectedGraphNode(n.label)
                    node_set[new_node.label] = new_node
                    node_stack.append(n)
                    current_new_node.neighbors.append(new_node)

        return new_root


def main():
    n0 = UndirectedGraphNode(0)
    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n0.neighbors = [n1, n2]
    n1.neighbors = [n0, n2]
    n2.neighbors = [n2]
    s = Solution()
    cloned = s.cloneGraph(n0)
    print "Cloned node's label: %s" % cloned.label


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)