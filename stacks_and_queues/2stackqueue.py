#!/usr/bin/python

'''
Solution to the problem:
    "Implement a Queue using two stacks"

Notes:
    Will be using the python list data structure as a stack, it natively has
    a push (append) and pop (pop) operation.
'''

class StackedQueue:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def enqueue(self, obj):
        self.left_stack.append(obj)

    def dequeue(self):
        result = None
        while len(self.left_stack) > 0:
            self.right_stack.append(self.left_stack.pop())
        if len(self.right_stack) > 0:
            result = self.right_stack.pop()
        while len(self.right_stack) > 0:
            self.left_stack.append(self.right_stack.pop())
        return result


if __name__ == '__main__':
    foo = StackedQueue()
    while True:
        in_data = str(input('Enqueue(1) or dequeue(2)? '))
        if in_data == '!':
            break
        elif in_data == '1':
            in_data = input('Value to be queued: ')
            if in_data == '!':
                break
            foo.enqueue(in_data)
            print('{} added to queue'.format(in_data))
        elif in_data == '2':
            print('Value from queue: {}'.format(foo.dequeue()))
        else:
            print('Error: invalid input')

