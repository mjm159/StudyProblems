#!/usr/bin/python

'''
You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in forward order, such that 
the 1's digit is at the tail of the list. Write a function that adds the two 
numbers and returns the sum as a linked list.

ex)
input: (6 -> 1 -> 7) + (2 -> 9 -> 5)
output: (9 -> 1 -> 2)

p.77 #2.5-2
'''

import linked_list_addition_1 as lla

def to_num(lst):
  '''
  Converts linked list to a num
  '''
  cur = lst.root
  num = 0
  while cur is not None:
    num = num * 10 + cur.val
    cur = cur.nxt
  return num

def to_list(num):
  res = str(num)
  lst = lla.LinkedList()
  for i in res:
    lst.add(int(i))
  return lst
    

if __name__ == '__main__':
  list1 = lla.LinkedList()
  list1.add(6)
  list1.add(1)
  list1.add(7)
  list1.print_list()
  list2 = lla.LinkedList()
  list2.add(2)
  list2.add(9)
  list2.add(5)
  list2.print_list()

  ### Solution ###
  res = to_num(list1) + to_num(list2)
  to_list(res).print_list()

