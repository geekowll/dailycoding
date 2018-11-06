"""
Given a root to a binary tree, implement serialize(root) which serializes tree into string and
deserialize(s) back into tree.

for ex:

class Node:
    def __init__(self,val,left=Node,right=Node):
	self.val = val
	self.left = left
	self.right = right

serialize => node = Node('root',Node('left',Node('left.left')),Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
