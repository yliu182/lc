# Python Quick Reference





## Sorting

```python
nums = [3, 1, 2]

nums.sort()                    # in-place, ascending
nums.sort(reverse=True)        # in-place, descending

sorted(nums)                   # returns new list, ascending
sorted(nums, reverse=True)     # returns new list, descending

# Custom sort with lambda
pairs = [(3, "x"), (1, "z"), (2, "y")]
pairs.sort(key=lambda x: x[0])          # by first element
pairs.sort(key=lambda x: x[1])          # by second element
pairs.sort(key=lambda x: (x[0], x[1]))  # by first, then second as tiebreaker
pairs.sort(key=lambda x: -x[0])         # descending by first element
```

## Iterating

### List

```python
nums = [10, 20, 30]

for val in nums:                  # values
    print(val)

for i in range(len(nums)):       # index
    print(i, nums[i])

for i, val in enumerate(nums):   # both
    print(i, val)
```

### Set

```python
s = {10, 20, 30}

for val in s:                     # values (no index, unordered)
    print(val)
```

### Dict

```python
d = {"a": 1, "b": 2, "c": 3}

for key in d:                     # keys
    print(key)

for val in d.values():            # values
    print(val)

for key, val in d.items():        # both
    print(key, val)
```

## Checking Membership (`in`)

### List — checks value (O(n))

```python
nums = [10, 20, 30]

20 in nums        # True
99 in nums        # False
99 not in nums    # True
```

### Set — checks value (O(1))

```python
s = {10, 20, 30}

20 in s           # True
99 in s           # False
```

### Dict — checks key (O(1))

```python
d = {"a": 1, "b": 2, "c": 3}

"a" in d              # True  (checks keys)
"z" in d              # False

1 in d.values()       # True  (checks values, O(n))
```

## Common List Operations

```python
nums = [1, 2, 3]

# Add
nums.append(4)             # [1, 2, 3, 4]          — add to end
nums.insert(0, 0)          # [0, 1, 2, 3, 4]       — insert at index
nums.extend([5, 6])        # [0, 1, 2, 3, 4, 5, 6] — append another list
nums += [7]                # [0, 1, 2, 3, 4, 5, 6, 7]

# Remove
nums.pop()                 # 7    — remove & return last
nums.pop(0)                # 0    — remove & return at index
nums.remove(3)             # removes first occurrence of value 3

# Access
nums[0]                    # first element
nums[-1]                   # last element
nums[1:3]                  # slice [1, 3)

# Info
len(nums)                  # length
min(nums)                  # minimum
max(nums)                  # maximum
sum(nums)                  # sum of all elements
nums.index(2)              # index of first occurrence of 2
nums.count(2)              # count occurrences of 2

# Other
nums.reverse()             # reverse in-place
nums[::-1]                 # reversed copy
list(zip([1,2], [3,4]))    # [(1,3), (2,4)] — pair elements
```

## Common Set Operations

```python
s = {1, 2, 3}

# Add / Remove
s.add(4)                   # {1, 2, 3, 4}
s.remove(4)                # {1, 2, 3}   — raises KeyError if missing
s.discard(99)              # no error if missing
s.pop()                    # remove & return arbitrary element
s.clear()                  # empty the set

# Set Math
a = {1, 2, 3}
b = {2, 3, 4}

a | b                      # {1, 2, 3, 4}  — union
a & b                      # {2, 3}        — intersection
a - b                      # {1}           — difference
a ^ b                      # {1, 4}        — symmetric difference

# Info
len(a)                     # size
a.issubset(b)              # is a ⊆ b?
a.issuperset(b)            # is a ⊇ b?
```

## Common Dict Operations

```python
d = {"a": 1, "b": 2}

# Add / Update
d["c"] = 3                 # add or overwrite
d.update({"d": 4, "e": 5}) # merge another dict

# Remove
d.pop("e")                 # 5    — remove & return value
d.pop("z", None)           # None — default if key missing
del d["d"]                 # delete key

# Access
d["a"]                     # 1    — raises KeyError if missing
d.get("a")                 # 1    — returns None if missing
d.get("z", 0)              # 0    — returns default if missing

# Info
len(d)                     # number of keys
list(d.keys())             # ["a", "b", "c"]
list(d.values())           # [1, 2, 3]
list(d.items())            # [("a", 1), ("b", 2), ("c", 3)]

# Useful patterns
from collections import defaultdict
dd = defaultdict(int)      # default value 0 for missing keys
dd["x"] += 1               # no KeyError, dd["x"] = 1

from collections import Counter
cnt = Counter([1,1,2,3,3,3])  # Counter({3: 3, 1: 2, 2: 1})
cnt.most_common(2)             # [(3, 3), (1, 2)]
```

## Tuple Operations

```python
# Create
t = (1, 2, 3)              # basic tuple
t = (1,)                   # single element (comma required!)
t = ()                     # empty tuple
t = tuple([1, 2, 3])       # from list

# Access
t[0]                       # first element
t[-1]                      # last element
t[1:3]                     # slice

# Unpack
a, b, c = (1, 2, 3)       # a=1, b=2, c=3
a, *rest = (1, 2, 3)      # a=1, rest=[2, 3]

# Info
len(t)                     # length
t.count(1)                 # count occurrences
t.index(2)                 # index of first occurrence

# Tuples are IMMUTABLE — cannot modify after creation
# Convert to list to modify, then back:
lst = list(t)
lst[0] = 99
t = tuple(lst)

# Common use: as dict keys (lists can't be dict keys)
d = {(0, 1): "start", (2, 3): "end"}
```
