import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    

  def insert(self, value):
    if self.value is None:
      self.value = value
    else:
      if self.value <= value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
      else:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    else:
      if self.right == None and self.left == None:
        return False
      if self.right.value <= target:
        return self.right.contains(target)
      elif self.left.value > target:
        return self.left.contains(target)

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, callback):
    q = []
    q.append(self)

    while len(q):
      current_node = q.pop(0)
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      callback(current_node.value)

# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):

    if node == None:
      return
    if node.left != None:
      node.left.in_order_dft(node.left)
    print(node.value)
    if node.right != None:
      node.right.in_order_dft(node.right)



  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    q = Queue()
    q.enqueue(node)
    
    while q.size > 0:
        node = q.dequeue()
        print(node.value)
        # node = None
        if node.left != None:
            q.enqueue(node.left)
        if node.right != None:
            q.enqueue(node.right)





  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    s = Stack()
    s.push(node)
    while s.size > 0:
        node = s.pop()
        print(node.value)
        if node.left != None:
            s.push(node.left)
        if node.right != None:
            s.push(node.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass