# Data Structures and Algorithms

p = (4,5)
x, y = p

print(x) # 4
print(y) # 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print (name) # ACME
print (date) # (2012, 12, 21)

name, shares, price, (year, mon, day) = data
print (name) # ACME
print (year) # 2012
print (mon) # 12
print (day) # 21

s = 'Hello'
a, b, c, d, e, = s
print (a) # H
print (b) # e
print (e) # o

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print (shares) # 50
print (price) # 91.1


# 1.2. Unpacking Elements from Iterables of Arbitrary Length
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com', '773-55-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print (name) # Dave
print (email) # dave@example.com
print (phone_numbers) # ['773-55-1212', '847-555-1212']


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print (trailing) # [10, 8, 7, 1, 9, 5, 10]

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y) # foo 1, 2

def do_bar(s):
    print('bar', s) # bar hello

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print (uname) # nobody
print (homedir) # /var/empty
print (sh) # /usr/bin/false

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print (name) # ACME
print (year) # 2012

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print (head) # 1
print (tail) # [10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print (sum(items)) # 36

# 1.3. Keeping the Last N Items
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('data.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*50)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print (q) # deque([1, 2, 3], maxlen=3)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print (q) # deque([1, 2, 3])

deque([1, 2, 3])
q.appendleft(4)
print(q) # 4, 1, 2, 3
deque([4, 1, 2, 3])
print(q.pop()) # 3
print(q) # deque([4, 1, 2])

# 1.4. Finding the Largest or Smallest N Items
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # [42, 37, 23]

people = [
  {'name': 'Alfons', 'age': '27', 'city': 'Iowa'},
  {'name': 'Bert', 'age': '67', 'city': 'B Hills'},
  {'name': 'Ceasar', 'age': '42', 'city': 'Trollhättan'},
  {'name': 'Dave', 'age': '32', 'city': 'Manhattan'}
 ]
young = heapq.nsmallest(3, people, key=lambda s: s['age'])
old = heapq.nlargest(3, people, key=lambda s: s['age'])

print (young) # [{'name': 'Alfons', 'age': '27', 'city': 'Iowa'}, {'name': 'Dave', 'age': '32', 'city': 'Manhattan'}, {'name': 'Ceasar', 'age': '42', 'city': 'Trollhättan'}]
print (old) # [{'name': 'Bert', 'age': '67', 'city': 'B Hills'}, {'name': 'Ceasar', 'age': '42', 'city': 'Trollhättan'}, {'name': 'Dave', 'age': '32', 'city': 'Manhattan'}]


# Converting/sorting data into a list where items are ordered as a heap
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print (heap) # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

# heapq.heappop() method pops off the first item and replaces it with the next smallest item
# To find the three smallest items you would do this:
print(heapq.heappop(heap)) # -4
print(heapq.heappop(heap)) # -1
print(heapq.heappop(heap)) # 2


# 1.5. Implementing a Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
