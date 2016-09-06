#!/usr/bin/python

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def store(self, val):
    cur = self.root
    if cur is None:
      self.root = Node(val)
      return
    while True:
      if val < cur.val:
        if cur.left is None:
          cur.left = Node(val)
          return
        else:
          cur = cur.left
      if val >= cur.val:
        if cur.right is None:
          cur.right = Node(val)
          return
        else:
          cur = cur.right

  def traverse(self):
    pass





def break_down(tree, lst):
  half = int(len(lst) / 2)
  tree.store(lst[half])
  print(lst[half], len(lst))
  if len(lst) == 1:
    return
  break_down(tree, lst[:half])
  print('\n')
  break_down(tree, lst[half+1:])
  print('\n')
  return


if __name__ == '__main__':
  test1 = [i for i in range(8)]
  tree1 = Tree()
  break_down(tree1, test1)

