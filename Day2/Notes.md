
# List

| Method      | Description                                             |
| ----------- | ------------------------------------------------------- |
| `append()`  | Adds an element to the end of the list                  |
| `extend()`  | Adds elements of another iterable to the list           |
| `insert()`  | Inserts an element at a specific position               |
| `remove()`  | Removes the first occurrence of a value                 |
| `pop()`     | Removes element at specified index (default last)       |
| `clear()`   | Removes all elements from the list                      |
| `index()`   | Returns the index of the first occurrence of an element |
| `count()`   | Returns number of occurrences of an element             |
| `sort()`    | Sorts the list                                          |
| `reverse()` | Reverses the list order                                 |
| `copy()`    | Returns a shallow copy of the list                      |

Total main **list methods = 11**

---

# Explanation with Examples

### 1. append()

Adds element at the end.

```python
lst = [1,2,3]
lst.append(4)

print(lst)
```

Output

```
[1,2,3,4]
```

---

### 2. extend()

Adds elements of another iterable.

```python
lst = [1,2]
lst.extend([3,4])

print(lst)
```

Output

```
[1,2,3,4]
```

---

### 3. insert()

```python
lst = [1,2,4]
lst.insert(2,3)

print(lst)
```

Output

```
[1,2,3,4]
```

---

### 4. remove()

```python
lst = [1,2,3,2]
lst.remove(2)

print(lst)
```

Output

```
[1,3,2]
```

(Removes first occurrence)

---

### 5. pop()

```python
lst = [10,20,30]

lst.pop()
print(lst)
```

Output

```
[10,20]
```

---

### 6. clear()

```python
lst = [1,2,3]
lst.clear()

print(lst)
```

Output

```
[]
```

---

### 7. index()

```python
lst = [10,20,30]

print(lst.index(20))
```

Output

```
1
```

---

### 8. count()

```python
lst = [1,2,2,3]

print(lst.count(2))
```

Output

```
2
```

---

### 9. sort()

```python
lst = [5,2,8,1]

lst.sort()

print(lst)
```

Output

```
[1,2,5,8]
```

---

### 10. reverse()

```python
lst = [1,2,3]

lst.reverse()

print(lst)
```

Output

```
[3,2,1]
```

---

### 11. copy()

```python
lst1 = [1,2,3]

lst2 = lst1.copy()

print(lst2)
```

Output

```
[1,2,3]
```

---

# Important Built-in Functions Used with Lists

These are **not list methods**, but frequently used with lists.

| Function   | Purpose                    |
| ---------- | -------------------------- |
| `len()`    | Returns number of elements |
| `max()`    | Maximum element            |
| `min()`    | Minimum element            |
| `sum()`    | Sum of elements            |
| `sorted()` | Returns sorted list        |

Example

```python
lst = [3,1,5]

print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
```

---
# Tuple

# Tuple Properties

| Property                      | Description                                |
| ----------------------------- | ------------------------------------------ |
| Ordered                       | Elements maintain insertion order          |
| Immutable                     | Elements cannot be modified after creation |
| Allows duplicates             | Same value can appear multiple times       |
| Indexed                       | Elements accessed using index              |
| Supports slicing              | Portions of tuple can be extracted         |
| Can store multiple data types | int, string, float, list, etc.             |

Example

```python
t = (10, "Python", 3.5)
```

---

# Tuple Methods (Only 2)

Python tuples provide **only two built-in methods**.

| Method    | Description                                 |
| --------- | ------------------------------------------- |
| `count()` | Returns number of occurrences of an element |
| `index()` | Returns index of first occurrence           |

---

## 1. `count()`

Counts occurrences of a value.

```python
t = (1,2,2,3,2)

print(t.count(2))
```

Output

```
3
```

---

## 2. `index()`

Returns first index of a value.

```python
t = (10,20,30,40)

print(t.index(30))
```

Output

```
2
```

---

# Common Built-in Functions Used with Tuples

These are **not tuple methods**, but they work with tuples.

| Function   | Description                |
| ---------- | -------------------------- |
| `len()`    | Returns number of elements |
| `max()`    | Returns largest element    |
| `min()`    | Returns smallest element   |
| `sum()`    | Returns sum of elements    |
| `sorted()` | Returns sorted list        |
| `tuple()`  | Converts iterable to tuple |

Example

```python
t = (4,1,7,3)

print(len(t))
print(max(t))
print(min(t))
```

Output

```
4
7
1
```

---

# Accessing Tuple Elements

### Indexing

```python
t = (10,20,30)

print(t[1])
```

Output

```
20
```

---

### Slicing

```python
t = (1,2,3,4,5)

print(t[1:4])
```

Output

```
(2,3,4)
```

---

# Sets

# Properties of Python Set

| Property                             | Description                                |
| ------------------------------------ | ------------------------------------------ |
| Unordered                            | Elements do not maintain insertion order   |
| Mutable                              | Elements can be added or removed           |
| Unique elements                      | Duplicate values are automatically removed |
| Unindexed                            | Elements cannot be accessed using index    |
| Iterable                             | Can be traversed using loops               |
| Supports mathematical set operations | Union, intersection, difference etc.       |

Example

```python
s = {1, 2, 3, 4}
```

---

# Python Set Methods

Python sets have the following **built-in methods**.

| Method                          | Description                              |
| ------------------------------- | ---------------------------------------- |
| `add()`                         | Adds an element to the set               |
| `update()`                      | Adds elements from another iterable      |
| `remove()`                      | Removes specified element                |
| `discard()`                     | Removes element if present               |
| `pop()`                         | Removes a random element                 |
| `clear()`                       | Removes all elements                     |
| `copy()`                        | Returns a shallow copy                   |
| `union()`                       | Returns union of sets                    |
| `intersection()`                | Returns intersection of sets             |
| `difference()`                  | Returns difference of sets               |
| `symmetric_difference()`        | Returns elements not common to both sets |
| `issubset()`                    | Checks if set is subset of another       |
| `issuperset()`                  | Checks if set is superset                |
| `isdisjoint()`                  | Checks if sets have no common elements   |
| `intersection_update()`         | Updates set with intersection            |
| `difference_update()`           | Updates set with difference              |
| `symmetric_difference_update()` | Updates set with symmetric difference    |

Total **17 commonly used set methods**

---

# Explanation with Examples

## 1. `add()`

```python
s = {1,2,3}

s.add(4)

print(s)
```

Output

```
{1,2,3,4}
```

---

## 2. `update()`

```python
s = {1,2}

s.update([3,4])

print(s)
```

Output

```
{1,2,3,4}
```

---

## 3. `remove()`

```python
s = {1,2,3}

s.remove(2)

print(s)
```

Output

```
{1,3}
```

(Removes element; error if not present)

---

## 4. `discard()`

```python
s = {1,2,3}

s.discard(4)
```

(No error if element not present)

---

## 5. `pop()`

```python
s = {10,20,30}

s.pop()

print(s)
```

(Removes random element)

---

## 6. `clear()`

```python
s = {1,2,3}

s.clear()

print(s)
```

Output

```
set()
```

---

## 7. `copy()`

```python
s1 = {1,2,3}

s2 = s1.copy()

print(s2)
```

Output

```
{1,2,3}
```

---

# Mathematical Set Operations

## 8. `union()`

```python
a = {1,2}
b = {2,3}

print(a.union(b))
```

Output

```
{1,2,3}
```

---

## 9. `intersection()`

```python
print(a.intersection(b))
```

Output

```
{2}
```

---

## 10. `difference()`

```python
print(a.difference(b))
```

Output

```
{1}
```

---

## 11. `symmetric_difference()`

```python
print(a.symmetric_difference(b))
```

Output

```
{1,3}
```

---

# Comparison Methods

### 12. `issubset()`

```python
a = {1,2}
b = {1,2,3}

print(a.issubset(b))
```

Output

```
True
```

---

### 13. `issuperset()`

```python
print(b.issuperset(a))
```

Output

```
True
```

---

### 14. `isdisjoint()`

```python
a = {1,2}
b = {3,4}

print(a.isdisjoint(b))
```

Output

```
True
```

---

# Update Operations

### 15. `intersection_update()`

Updates set with common elements.

### 16. `difference_update()`

Removes common elements.

### 17. `symmetric_difference_update()`

Updates set with non-common elements.

---

# Built-in Functions Used with Sets

| Function   | Description             |
| ---------- | ----------------------- |
| `len()`    | Number of elements      |
| `max()`    | Maximum element         |
| `min()`    | Minimum element         |
| `sum()`    | Sum of numeric elements |
| `sorted()` | Returns sorted list     |

Example

```python
s = {3,1,5}

print(len(s))
print(max(s))
print(min(s))
```

---

# Dictionary

# Properties of Dictionary

| Property                 | Description                                 |
| ------------------------ | ------------------------------------------- |
| Key–Value Pair           | Each element consists of a key and a value  |
| Mutable                  | Elements can be added, modified, or removed |
| Ordered (Python ≥3.7)    | Maintains insertion order                   |
| Keys are unique          | Duplicate keys are not allowed              |
| Values can be duplicated | Multiple keys can have the same value       |
| Keys must be immutable   | e.g., int, string, tuple                    |
| Indexed by keys          | Values accessed using keys                  |

Example

```python
d = {"name": "Alice", "age": 25}
```

---

# Dictionary Methods

Python dictionaries provide the following **built-in methods**.

| Method         | Description                                |
| -------------- | ------------------------------------------ |
| `clear()`      | Removes all elements                       |
| `copy()`       | Returns a shallow copy of dictionary       |
| `fromkeys()`   | Creates dictionary from given keys         |
| `get()`        | Returns value of specified key             |
| `items()`      | Returns key-value pairs                    |
| `keys()`       | Returns all keys                           |
| `values()`     | Returns all values                         |
| `pop()`        | Removes specified key                      |
| `popitem()`    | Removes last inserted key-value pair       |
| `setdefault()` | Returns value of key, inserts if missing   |
| `update()`     | Updates dictionary with another dictionary |

Total **11 dictionary methods**

---

# Explanation with Examples

## 1. `clear()`

Removes all items.

```python
d = {"a":1,"b":2}
d.clear()

print(d)
```

Output

```
{}
```

---

## 2. `copy()`

Creates shallow copy.

```python
d1 = {"a":1,"b":2}

d2 = d1.copy()

print(d2)
```

Output

```
{'a':1,'b':2}
```

---

## 3. `fromkeys()`

Creates dictionary with given keys.

```python
keys = ("a","b","c")

d = dict.fromkeys(keys,0)

print(d)
```

Output

```
{'a':0,'b':0,'c':0}
```

---

## 4. `get()`

Returns value of key.

```python
d = {"name":"Alice"}

print(d.get("name"))
```

Output

```
Alice
```

---

## 5. `items()`

Returns key-value pairs.

```python
d = {"a":1,"b":2}

print(d.items())
```

Output

```
dict_items([('a',1),('b',2)])
```

---

## 6. `keys()`

Returns all keys.

```python
d = {"a":1,"b":2}

print(d.keys())
```

Output

```
dict_keys(['a','b'])
```

---

## 7. `values()`

Returns all values.

```python
d = {"a":1,"b":2}

print(d.values())
```

Output

```
dict_values([1,2])
```

---

## 8. `pop()`

Removes a key.

```python
d = {"a":1,"b":2}

d.pop("a")

print(d)
```

Output

```
{'b':2}
```

---

## 9. `popitem()`

Removes last inserted item.

```python
d = {"a":1,"b":2}

d.popitem()

print(d)
```

Output

```
{'a':1}
```

---

## 10. `setdefault()`

Returns value of key, adds key if missing.

```python
d = {"a":1}

d.setdefault("b",2)

print(d)
```

Output

```
{'a':1,'b':2}
```

---

## 11. `update()`

Updates dictionary with another dictionary.

```python
d = {"a":1}

d.update({"b":2})

print(d)
```

Output

```
{'a':1,'b':2}
```

---

# Built-in Functions Used with Dictionary

| Function   | Description                       |
| ---------- | --------------------------------- |
| `len()`    | Returns number of key-value pairs |
| `type()`   | Returns object type               |
| `sorted()` | Returns sorted keys               |
| `max()`    | Maximum key                       |
| `min()`    | Minimum key                       |

Example

```python
d = {"a":3,"b":1,"c":5}

print(len(d))
```

Output

```
3
```

---

