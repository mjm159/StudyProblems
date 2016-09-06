#!/usr/bin/python

'''
You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order, such that 
the 1's digit is at the head of the list. Write a function that adds the two 
numbers and returns the sum as a linked list.

p.77 #2.5-1

ex)
input (7 -> 1 -> 6) + (5 -> 9 -> 2)
output 2 -> 1 -> 9
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.nxt = None


class LinkedList:
  def __init__(self):
    self.root = None

  def add(self, val):
    if self.root is None:
      self.root = Node(val)
      return
    marker = self.root
    while marker.nxt is not None:
      marker = marker.nxt
    marker.nxt = Node(val)

  def print_list(self):
    cur = self.root
    res = ''
    while cur is not None:
      res = ''.join((res, '{} -> '.format(cur.val)))
      cur = cur.nxt
    res = ''.join((res, 'None'))
    print(res)

def to_num(root):
  '''
  Turns linked list into a number
  '''
  num = 0
  multiplier = 1
  cur = root
  while cur is not None:
    num += cur.val * multiplier
    multiplier *= 10
    cur = cur.nxt
  return num

def build_list(res):
  lst = LinkedList()
  res = str(res)
  for i in res[::-1]:
    lst.add(int(i))
  return lst


if __name__ == '__main__':
  list1 = LinkedList()
  list1.add(7)
  list1.add(1)
  list1.add(6)
  list1.print_list()
  list2 = LinkedList()
  list2.add(5)
  list2.add(9)
  list2.add(2)
  list2.print_list()

  ###### Solution #######
  res = to_num(list1.root) + to_num(list2.root)
  res = build_list(res)
  res.print_list()











