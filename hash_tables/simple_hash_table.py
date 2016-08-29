#!/usr/bin/python

'''
Simple hash table implementation
'''

import random
from collections import namedtuple

Node = namedtuple('Node','key data')
table = [[] for i in range(20)]
values = [Node(x,random.random()) for x in range(43)]


#class Node:
#  def __init__(self, key, data):
#    self.key = key
#    self.data = data

def print_table(tbl):
  for line in tbl:
    print(line)

def hash_it(key):
  # Using prime number 131 to salt the randomness
  salt1 = 131
  salt2 = 103
  return ((key * salt1) / salt2) % len(table)

def store_it(node):
  hash_key = hash_it(node.key)
  for index in range(len(table[hash_key])):
    if table[hash_key][index] == node.key:
      table[hash_key][index].remove(index)
      break
  table[hash_key].append(node)

def retrieve_it(key):
  hash_key = hash_it(key)
  for item in table[hash_key]:
    if item.key == key:
      return item
  return None
  

if __name__ == '__main__':
  # Populate table
  print('table initially: ')
  print_table(table)
  for item in values:
    store_it(item)
  print('\ntable post fill: ')
  print_table(table)

  print('\nretrieving keys: ')
  print(retrieve_it(13))
  print(retrieve_it(1))
  print(retrieve_it(10))
  print(retrieve_it(8))
