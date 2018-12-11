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

# 1.6. Mapping Keys to Multiple Values in a Dictionary

'''
A dictionary is a mapping where each key is mapped to a single value.
If you want to map keys to multiple values, you need to store the multiple values
in another container such as a list or set. For example, you might make dicts
like this:
'''

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

d = defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

'''
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# using a defaultdict simply leads to much cleaner code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
'''

# 1.7. Keeping Dictionaries in Order
'''
To control the order of items in a dictionary you can use an OrderedDict from
the collections module. It exactly preserves the original insertion order of
data when iterating. For example:
'''
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['baz'] = 3
d['qux'] = 4

# Outputs "foo 1", "bar 2", "baz 3", "qux 4"
for key in d:
    print(key, d[key])

'''
An OrderedDict can be particularly useful when you want to build a mapping that
you may want to later serialize or encode into a different format. For example
if you want to precisely control the order of fields appearing in a JSON enconding
first buildning the data in the OrderedDict will do the trick:
'''
import json
print(json.dumps(d)) #{"foo": 1, "bar":2, "baz": 3, "qux": 4}

'''
Consider a dictionary that maps stock names to prices
'''
#1.8. Calculating with Dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

'''
In order to perform useful calculations on the dctionary contents, it is often
useful to invert the keys and values of the dict using zip(). For example,
here is a how to find the minimum price and stock name:
'''

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print (min_price) # (10.75, 'FB')
print (max_price) # (612.78, 'AAPL')

# Similarly to rank the data use zip() with sorted() as in the following:
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print (prices_sorted) # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

'''
If you try to perform common data reductions on a dictionary, you'll find that
they only process the keys, not the values, for example:
'''

print (min(prices)) # AAPL
print (max(prices)) # IBM

'''
This is probably not what you want because you're actually trying to perform a
calculation involving the dictionary values. You might try to fix this using
the values() method of a dictionary:
'''

print (min(prices.values())) # 10.75
print (max(prices.values())) # 612.78

'''
Unfortunately this is often not exactly what you want either. For example
you may want to know information about the corresponding keys (eg. which stock
has the lowest price?)

You can get the key corresponding to the min or max value if you supply a key
function to min() or max(). For example:
'''
print (min(prices, key=lambda k: prices[k])) # returns 'FB'
print (max(prices, key=lambda k: prices[k])) # returns 'AAPL'

'''
However to get the minimum value, you'll need to perform an extra lookup step.
For example:
'''

min_value = prices[min(prices, key=lambda k: prices[k])]
print (min_value) # 10.75

'''
The solution involving zip() solves the problem by "inverting" the dictionary
into a sequence of (value, key) pairs. When performing comparisons on such
tuples, the value element is compared first, followed by the key. This
gives you exactly the behaviour that you want and allows reductions and sorting
to be easily performed on the dictionary contents using a single statement.

It should be noted that in calculations involving (value, key) pairs, the key
will be used to determine the result in instances where multiple entries happen
to have the same value. For instance, in calculations such as min() and max()
the entry with the smallest or largest key will be returned if there happen
to be a duplicate values. For example
'''

prices = {'AAA': 45.23, 'ZZZ': 45.23}
print (min(zip(prices.values(), prices.keys()))) # (45.23, 'AAA')
print (max(zip(prices.values(), prices.keys()))) # (45.23, 'ZZZ')

# 1.9. Finding Commonalities in Two Dictionaries
'''
If you have 2 dicts and want to find out what they might have in common
(same keys, values etc) Consider 2 dictionaries:
'''

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

'''
To find out what the 2 dicts have in common, simply perform common set operations
using keys() or items() methods, for example:
'''

# Find keys in common
print(a.keys() & b.keys()) # { 'x', 'y'}

# Find keys in a that are not in b
print (a.keys() - b.keys()) # {'z'}

# Find (key, value) pairs in common
print (a.items() & b.items()) # {('y', 2)}

'''
These kinds of operations can also be used to alter or filter dictionary
contents. For example, suppose you want to make a new dictionary with selected
keys removed. Here is some sample code using a dictionary comprehension
'''

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print (c) # {'y': 2, 'x': 1}
