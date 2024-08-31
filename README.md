# pynq
Python Integrated Query
> ⚠️ work in progress

# Documentation
> ⚠️ As I am working on the documentation and refactoring the code you can find examples on how to use the `Enumerable` class in the [enumerables tests](./src/enumerables_test.py). I will add an example for each method as soon as possible

## Methods of `Enumerable`
### `of(values: Iterable[T]) -> 'Enumerable[T]'`
Creates an `Enumerable` object from a collection of values.

### `empty() -> 'Enumerable[T]'`
Creates an empty `Enumerable` object.

### `where(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Filters the values of the `Enumerable` object based on a predicate.

### `select(selector: Callable[[T], T]) -> 'Enumerable[T]'`
Projects the values of the `Enumerable` object based on a selector.

### `select_many(selector: Callable[[T], Iterable[T]]) -> 'Enumerable[T]'`
Flattens the values of the `Enumerable` object based on a selector.

### `distinct() -> 'Enumerable[T]'`
Removes duplicate values from the `Enumerable` object.

### `distinct_by(key_selector: Callable[[T], T]) -> 'Enumerable[T]'`
Removes duplicate values from the `Enumerable` object based on a key selector.

### `take(count: int) -> 'Enumerable[T]'`
Takes the first `count` values from the `Enumerable` object.

### `take_while(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Takes values from the `Enumerable` object while the predicate is true.

### `skip(count: int) -> 'Enumerable[T]'`
Skips the first `count` values from the `Enumerable` object.

### `skip_while(predicate: Callable[[T], bool]) -> 'Enumerable[T]'`
Skips values from the `Enumerable` object while the predicate is true.

### `aggregate(func: Callable[[T, T], T]) -> T`
Applies an accumulator function over the values of the `Enumerable` object.

### `aggregate_with_seed(func: Callable[[T, T], T], seed: T) -> T`
Applies an accumulator function over the values of the `Enumerable` object with a seed/initial value.

### `count() -> int`
Counts the number of values in the `Enumerable` object.

### `count_where(predicate: Callable[[T], bool]) -> int`
Counts the number of values in the `Enumerable` object that satisfy a predicate.

### `concat(values: Iterable[T]) -> 'Enumerable[T]'`
Concatenates the values of the `Enumerable` object with another collection of values.

### `first() -> T`
Gets the first value of the `Enumerable` object. If the `Enumerable` object is empty, it returns `None`.

### `first_where(predicate: Callable[[T], bool]) -> T`
Gets the first value of the `Enumerable` object that satisfies a predicate.

### `last() -> T`
Gets the last value of the `Enumerable` object. If the `Enumerable` object is empty, it returns `None`.

### `last_where(predicate: Callable[[T], bool]) -> T`
Gets the last value of the `Enumerable` object that satisfies a predicate.

### `sort(key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]'`
Sorts the values of the `Enumerable` object based on a key.

### `sort_by(key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]'`
Sorts the values of the `Enumerable` object based on a key.

### `reverse() -> 'Enumerable[T]'`
Reverses the values of the `Enumerable` object.

### `foreach(action: Callable[[T], None]) -> None`
Performs an action on each value of the `Enumerable` object.

### `any(predicate: Callable[[T], bool]) -> bool`
Checks if any value in the `Enumerable` object satisfies a predicate.

### `all(predicate: Callable[[T], bool]) -> bool`
Checks if all values in the `Enumerable` object satisfy a predicate.

### `is_empty() -> bool`
Checks if the `Enumerable` object is empty.

### `to_list() -> List[T]`
Converts the `Enumerable` object to a list.

### `to_set() -> set[T]`
Converts the `Enumerable` object to a set.
