#!/usr/bin/python

'''
Refer to problem 2.4 p. 77 in Cracking the coding interview.

Problem:
  Write code to partition a linked list around a value x such that all nodes less
  than x come before all nodes greater than or equal to x.
'''


class Node:
  '''
  Node in a liked list
  '''
  def __init__(self, data):
    self.data = data
    self.nxt = None


def sorta_sort(head, n):
  '''
  Moves around nodes to solve problem statement
  '''
  cur = head
  prev = head
  hit_pivot = False
  while cur is not None:
    if cur.data >= n:
      hit_pivot = True
    if cur.data < n and hit_pivot:
      prev.nxt = cur.nxt
      cur.nxt = head
      head = cur
      cur = prev
    else:
      prev = cur
      cur = cur.nxt
  return head


def print_list(marker):
  res = ''
  while marker is not None:
    res = ''.join([res, ' ', str(marker.data)])
    marker = marker.nxt
  print(res)


if __name__ == '__main__':
  prob_list = [4,5,7,1,3,8,5,9,6,4,5]
  head = Node(prob_list[0])
  cur = head
  for i in prob_list[1:]:
    temp = Node(i)
    cur.nxt = temp
    cur = cur.nxt
  print_list(head)
  head = sorta_sort(head, 5)
  print_list(head)



