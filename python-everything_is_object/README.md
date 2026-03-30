![Python programming](Python_programming.png)

# Understanding Python Objects: Mutable vs Immutable

In Python, everything is an object. Whether it's a number, a string, or a list,
every piece of data is an object stored somewhere in memory. In this blog post,
we will explore how Python handles objects, the difference between mutable and
immutable objects, and why it matters when writing Python code.

## id and type
Every object in Python has two important properties:
* `type()` tells you what kind of object it is
* `id()` tells you where it is stored in memory
```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # 140234567891234
```

## Immutable objects
Immutable objects cannot be modified after they are created. If you try to
change them, Python creates a new object in memory instead.
Examples of immutable objects: `int`, `float`, `str`, `tuple`
```python
a = 89
b = 89
print(a is b)  # True (same object in memory, integer caching)
```
```python
a = (1, 2)
b = (1, 2)
print(a is b)  # False (different objects in memory)
```

Python also applies two important optimizations for immutable objects:
* Integer caching: Python reuses the same object for small integers
* String interning: Python reuses the same object for certain strings
```python
a = "Best School"
b = "Best School"
print(a is b)  # True (string interning)
```

## Mutable objects
Mutable objects can be modified after they are created. Python modifies the
same object in memory instead of creating a new one.
Examples of mutable objects: `list`, `dict`, `set`
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4] (same object!)
```

## Why does it matter?
Python treats mutable and immutable objects very differently:
* For immutable objects, Python can optimize memory by reusing the same object
(integer caching, string interning)
* For mutable objects, each new object is always a separate object in memory
```python
a = "Best School"
b = "Best School"
print(a is b)  # True (string interning)
```
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)  # False (different objects)
```

## How arguments are passed to functions
In Python, arguments are passed by object reference. This means the function
receives a reference to the same object in memory.

* For immutable objects, the function cannot modify the original object:
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1 (unchanged)
```

* For mutable objects, the function can modify the original object:
```python
def append_four(l):
    l.append(4)

my_list = [1, 2, 3]
append_four(my_list)
print(my_list)  # [1, 2, 3, 4] (modified!)
```

## Conclusion
Understanding the difference between mutable and immutable objects is essential
in Python. It helps you avoid unexpected bugs, especially when passing objects
to functions or copying lists. Always remember: use `=` to copy a reference,
and `.copy()` to create a real copy of a list!
