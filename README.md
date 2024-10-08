# pynq
Python Integrated Query

# Examples
## Method Chaining
This is the preferred way to chain methods since it implements all of the methods which are stated at the end of this document. Also if you have an LSP installed then all of the methods will be shown in your IDE. Here is an example on how to use it:

```python
from enumerables import Enumerable

def factorial(n: int) -> int: return 1 if n == 0 else n * factorial(n - 1)

result: int = (
    Enumerable().of(range(10))
    .select(factorial)
    .where(lambda x: x % 2 == 0)
    .aggregate(lambda x, y: x + y)
)

print(result)
```

## Piping
You can also use pipes to chain methods.
- To `map`/`select` you pipe a `Selector`.
- To `filter`/`where` you pipe a `Predicate`.
- To `reduce`/`aggregate` you pipe a `Accumulator`.
- To do some sort of `foreach` with methods that don't return anyting you should use `Action`

Pipes only support the Functions mentioned above and functions
which depend on only one Enumerable parameter (`f(e: Enumerable) -> any`) like `to_list` or `to_set`.
If you want more complex queries then please use the method chaining.

```python
from enumerables import Enumerable, Selector, Predicate, Accumulator, Action

def factorial(n: int) -> int: return 1 if n == 0 else n * factorial(n - 1)

result: int = (
    Enumerable().of(range(10))
    | Selector(factorial)
    | Predicate(lambda x: x % 2 == 0)
    | Accumulator(lambda x, y: x + y)
)

print(result)

Enumerable().of(range(10)) | Action(print)
```

# Enumerable

The `Enumerable` class provides LINQ-like operations for collections in Python. It allows for easy manipulation and querying of collections.

## Class Methods

### `of(values: Iterable[T]) -> 'Enumerable[T]'`
Creates an `Enumerable` object from a collection of values.

### `empty() -> 'Enumerable[T]'`
Creates an empty `Enumerable` object.

### `where(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Filters values based on a predicate.

### `select(selector: Callable[[T], T]) -> 'Enumerable[T]'`
Projects values based on a selector.

### `select_many(selector: Callable[[T], Iterable[T]]) -> 'Enumerable[T]'`
Flattens and projects values based on a selector.

### `distinct() -> 'Enumerable[T]'`
Removes duplicate values.

### `distinct_by(key_selector: Callable[[T], T]) -> 'Enumerable[T]'`
Removes duplicates based on a key selector.

### `take(count: int) -> 'Enumerable[T]'`
Takes the first `count` values.

### `take_while(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Takes values while a predicate is true.

### `skip(count: int) -> 'Enumerable[T]'`
Skips the first `count` values.

### `skip_while(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Skips values while a predicate is true.

### `aggregate(func: Callable[[T, T], T]) -> T`
Applies an accumulator function over the values.

### `aggregate_with_seed(func: Callable[[T, T], T], seed: T) -> T`
Applies an accumulator function with a seed value.

### `count() -> int`
Counts the number of values.

### `count_where(predicate: Callable[[T], bool]) -> int`
Counts values satisfying a predicate.

### `concat(values: Iterable[T]) -> 'Enumerable[T]'`
Concatenates with another collection of values.

### `first() -> T`
Gets the first value, or `None` if empty.

### `first_where(predicate: Callable[[T], bool]) -> T`
Gets the first value satisfying a predicate.

### `last() -> T`
Gets the last value, or `None` if empty.

### `last_where(predicate: Callable[[T], bool]) -> T`
Gets the last value satisfying a predicate.

### `sort(key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]'`
Sorts values based on a key.

### `sort_by(key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]'`
Sorts values based on a key (alias for `sort`).

### `reverse() -> 'Enumerable[T]'`
Reverses the values.

### `foreach(action: Callable[[T], None]) -> None`
Performs an action on each value.

### `any(predicate: Callable[[T], bool]) -> bool`
Checks if any value satisfies a predicate.

### `all(predicate: Callable[[T], bool]) -> bool`
Checks if all values satisfy a predicate.

### `is_empty() -> bool`
Checks if the collection is empty.

### `to_list() -> List[T]`
Converts to a list.

### `to_set() -> set[T]`
Converts to a set.

### `combine(other: 'Enumerable[T]') -> 'Enumerable[T]'`
Combines with another `Enumerable` object.

### `zip(other: 'Enumerable[T]') -> 'Enumerable[Tuple[T, T]]'`
Zips with another `Enumerable` object.

### `intersect(self, other: 'Enumerable[T]') -> 'Enumerable[T]'`
The `intersect` method is used to get the intersection of this Enumerable object with another Enumerable object.

### `without(self, other: 'Enumerable[T]') -> 'Enumerable[T]'`
The `without` method is used to get the values of this Enumerable object that are not in another Enumerable object.

### Operator Overloads

#### `__or__(func: Callable) -> UnionType`
Enables the use of operators for chaining operations using the `|` (pipe). For example:
```python
result: int = (
    Enumerable().of(range(10))
    | Selector(lambda x: x * 2)
    | Predicate(lambda x: x > 10)
    | Accumulator(lambda x, y: x + y)
)
```

#### `__iter__(self) -> Iterable[T]`
Overwrites the `iter` function and returns an iterator of the enumerable.
