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