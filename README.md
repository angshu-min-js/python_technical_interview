# Preparing for a technical interview, "the good the bad and the ugly"

```	c
/*
      Well, every one needs a safety Pig :D
            _
     _._ _..._ .-',     _.._(`))
    '-. `     '  /-._.-'    ',/
       )         \            '.
      / _    _    |             \
     |  a    a    /              |
     \   .-.                     ;  
      '-('' ).-'       ,'       ;
         '-;           |      .'
            \           \    /
            | 7  .__  _.-\   \
            | |  |  ``/  /`  /
           /,_|  |   /,_/   /
              /,_/      '`-'
*/   
```


Preparing for anything is difficult and specially a technical interview if you don't a CS degree. But it's not impossible, the big secret is ......."Practice".
Well, isn't that obvious but that's really all to it. Let me summarise:
- Pick a language, Python is really easy to start with, you don't have to worry about learning the language and you can easily dive into solving problems and algorithms
- Solve problems and learn algorithms, start with the basics and slowly you can move forward, SOLVE PROBLEMS EVERYDAY!
- Learn JAVA. After you're comfortable with python and basic algorithm you can move on to JAVA. JAVA really good with data structures and if you want to dive deep and learn Algorithms and Data Structures JAVA is the best. Period.

### Few online python resourses:
1. https://www.coursera.org/specializations/python : This is an excellent course!
2. https://classroom.udacity.com/courses/cs101 : Learn how  basic search engine and social network works
3. https://classroom.udacity.com/courses/ud513 : It can help you to start with your interview process, understand the basic mechanics
4. https://classroom.udacity.com/courses/cs215 : Algorithms - Intermediate Level
5. https://classroom.udacity.com/courses/cs212 : Algorithms - Intermediate Level
6. http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html : Title says it all :D


# Below is a summary of python and basic algorithms and data structures

	Well, After I'm done with python I would make notes for JAVA, that's a promise :D
	


### Declaration/Initialization
- Remember values, not variables, have data types.
- A variable can be reassigned to contain a different data type.
```
answer = 42
answer = "The answer is 42."
Data Types
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None
```
### Simple Logging
```
print "Printed!"
```
### Conditionals
```
if cake == "delicious":
    return "Yes please!"
elif cake == "okay":
    return "I'll have a small piece."
else:
    return "No, thank you."
Loops
for item in list:
    print item

while (total < max_val):
    total += values[i]
    i += 2
```

### Functions
```
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
```
### Classes
```
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
```

### Algorithm Analysis

- https://visualgo.net
- https://www.toptal.com/developers/sorting-algorithms/
```
import time

def sum_of_n1(n):
    start = time.time()
    sum = 0
    for i  in range(0, n):
        sum = sum + i
    end = time.time()
    return sum, end-start
print "Iterative:", sum_of_n1(5000000)

def sum_of_n2(n):
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()
    return sum, end-start
print "Algorithm (Summation Eqn):", sum_of_n2(5000000)

#Iterative: (12499997500000L, 0.9650001525878906)
#Algorithm: (Summation Eqn) (12500002500000L, 0.0)
#Iterative solutions takes more time and less accurate
```
#### Big-O Notation
- The order of magnitude function describes the part of T(n) that increases the
- fastest as the value of n increases. Order of magnitude is often called Big-O
- notation (for "order") and written as O(F(n)).  It provides a useful
- approximation to the actual number of steps in the computation.

```
a = 5
b = 6
c = 10 # 3 assignment
for i in range(n):
    for j in range(n): # n^2 iteration
        x = i * i
        y = j * j
        z = i * j # 3 assignment
for k in range(n): # n
    w = a * k + 45
    v = b * b # 2
d = 33 # 1

# So, T(n) = 3 + 3n^2 + 2n + 1 =  4 + 3n^2 + 2n : O(n^2) --> Big-O, Quadratic (n^2)
```
- List: append: O(1), concatenation: O(k)

```
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print ("append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

# ('concat ', 6.391950280176704, 'milliseconds')
# ('append ', 0.1982510243736293, 'milliseconds')
# ('comprehension ', 0.09311756341678024, 'milliseconds')
# ('list range ', 0.03239667522277667, 'milliseconds')
```

```
import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange (%d) in x"%i,
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" %(i, lst_time, d_time))


10000,      0.139,      0.002
30000,      0.401,      0.002
50000,      0.742,      0.002
70000,      1.144,      0.002
90000,      1.426,      0.002
110000,      1.816,      0.002
130000,      2.106,      0.002
150000,      2.425,      0.002
170000,      2.815,      0.002
190000,      3.268,      0.002
210000,      3.989,      0.002
230000,      3.714,      0.002
250000,      4.359,      0.002
270000,      4.543,      0.002
290000,      4.642,      0.003
310000,      5.016,      0.002
330000,      5.465,      0.003
350000,      5.577,      0.003
370000,      5.818,      0.002
```
- List is O(n) and Dictionary is O(1)



### Data Structures

- Stack: Addition & removal at top. LIFO
- Queue: Addition & removal different ends. FIFO.
- Deque : Double-ended queue. Hybrid. Both end-start
- Linked List: The basic building block for the linked list implementation is the node.
- Unordered List: Collection of nodes

### Searching and Sorting

- Binary Search: Finding the mid and searching, O(log(n))
- Recursion: Calling function by the function itself

  In practice if we were to use recursion to solve this problem we should use a hash table
  to store and fetch previously calculated results. This will increase the space needed
  but will drastically improve the runtime efficiency.

- Bubble Sort: Naive Approach, compare two and switch, Efficiency: O(n^2), Space: O(1)
- Selection Sort: Similar to bubble but swaps the largest/smallest and so on per pass. Efficiency: O(n^2), Space: O(1)
- Insertion Sort: Again it's a naive approach, compares with a sub-list. Efficiency: O(n^2), Space: O(1)
- Shell Sort: Efficiency: O(n^3/2), Space: O(1)
- Merge Sort: Divide & Conquer, Efficiency: O(log(n)), Space: O(n)
- Quick Sort: Select a Pivot and Compare,  Efficiency: worst - O(n^2) average - O(log(n)), Space: O(1)

### Maps and Hashing
- Map --> dictionary
- Map is a 'set' based DS (no sequence) kinda like Arrays which is a 'list' based DS
- Map = `<key, value>`
- keys are unique sets
- In Python, the map concept appears as a built-in data type called a dictionary.

- Hasting: Take last few digits of the number and divide it with a consistent number and use the remainder to store the number
```
0123456 ---> 56/10 = 5, Remainder: 6
{6: 0123456}
```
- This helps to achieve a constant lookup
- Collison: To avoid collision use a different hash function or use buckets (http://www.cs.cmu.edu/~clo/www/CMU/DataStructures/Lessons/lesson11_2.htm)
```
Load Factor = Number of Entries / Number of Buckets
```
- The purpose of a load factor is to give us a sense of how "full" a hash table is.
- A Python dictionary is a hash map

### Trees
- Its an extension of a linked list
- must be connected and shouldn't have cycles
- Depth First Search Traversal: Pre-Order, In-Order, Post-Order

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/tree.jpg" width="256">

  BFS: A, B, C, D, E, F

  In-order: D, B, E, F, A, C

  Pre-order: A, B, D, E, F, C
  
  Post-order: D, F, E, B, C, A


### Heaps
- Increasing/decreasing order; max heap, min heap
- Heapify: Reordering the list according to the heap property

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/heap1.JPG" width="512">
<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/heap2.JPG" width="512">

### Red Black Trees: Balanced Tree
- Values are black or Red
- All nodes which doesnt have two leaf must have null leaf nodes
- If a node is black, its children must be black
- All paths from node to descendant must have equal black nodes
- RBT + BST rules

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/redblacktree1.JPG" width="256">
<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/redblacktree2.JPG" width="256">

### Graphs
- Network
- Similar to tree; is a spedific type of graph
- Nodes and Edges
<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph.JPG" width="512">

- Disconnected: Disconnected graphs are very similar whether the graph's directed or undirected—there is some vertex or group of vertices that have no connection with the rest of the graph.

- Weakly Connected: A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.

- Connected: Here we only use "connected graph" to refer to undirected graphs. In a connected graph, there is some path between one vertex and every other vertex.

- Strongly Connected: Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A.

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph1.JPG" width="256">

- Cycles:
```
  G->R->A->P->H->G
  R->A->P->R
  R->A->P->S->R
```
- U doesn't have a path, if converted every edge to an undirected edge, wouldn't be connected, weakly connected

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph_adjacent_matrix.JPG">
- Efficiency: O(1), Space: O(n^2)

<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph_adjacent_list.JPG">
- Efficiency: O(n), Space: O(n)-->O(n^2)

- DFS --> Stack/recursion
<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph_dfs.JPG" width="256">

- BFS --> Queue
<img src="https://github.com/angshu-min-js/python_technical_interview/blob/master/images/graph_bfs.JPG" width="256">

- O(|E| + |V|)

