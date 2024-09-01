from typing import Iterable, Callable, TypeVar, List
from itertools import islice, takewhile, dropwhile
from functools import reduce


T = TypeVar('T')

def where(values: Iterable[T], predicate: Callable[[T], bool]) -> Iterable[T]:
    return filter(predicate, values)

def select(values: Iterable[T], selector: Callable[[T], T]) -> Iterable[T]:
    return map(selector, values)

def select_many(values: Iterable[T], selector: Callable[[T], Iterable[T]]) -> Iterable[T]:
    return (x for y in values for x in selector(y))

def distinct(values: Iterable[T]) -> Iterable[T]:
    seen = set()
    return (x for x in values if x not in seen and not seen.add(x))

def distinct_by(values: Iterable[T], key_selector: Callable[[T], T]) -> Iterable[T]:
    seen = set()
    return (x for x in values if (key := key_selector(x)) not in seen and not seen.add(key))

def take(values: Iterable[T], count: int) -> Iterable[T]:
    return islice(values, count)

def take_while(values: Iterable[T], predicate: Callable[[T], bool]) -> Iterable[T]:
    return takewhile(predicate, values)

def skip(values: Iterable[T], count: int) -> Iterable[T]:
    return islice(values, count, None)

def skip_while(values: Iterable[T], predicate: Callable[[T], bool]) -> Iterable[T]:
    return dropwhile(predicate, values)

def aggregate(values: Iterable[T], func: Callable[[T, T], T]) -> T:
    return reduce(func, values)

def aggregate_with_seed(values: Iterable[T], func: Callable[[T, T], T], seed: T) -> T:
    return reduce(func, values, seed)

def count(values: Iterable[T]) -> int:
    return sum(1 for _ in values)

def count_where(values: Iterable[T], predicate: Callable[[T], bool]) -> int:
    return sum(1 for x in values if predicate(x))

def concat(values: Iterable[T], other_values: Iterable[T]) -> Iterable[T]:
    return list(values) + list(other_values)

def first(values: Iterable[T]) -> T:
    return next(iter(values), None)

def first_where(values: Iterable[T], predicate: Callable[[T], bool]) -> T:
    return next((x for x in values if predicate(x)), None)

def last(values: Iterable[T]) -> T:
    return next(reversed(list(values)), None)

def last_where(values: Iterable[T], predicate: Callable[[T], bool]) -> T:
    return next(reversed([x for x in values if predicate(x)]), None)

def sort(values: Iterable[T], key: Callable[[T], T], reverse: bool = False) -> Iterable[T]:
    return sorted(values, key=key, reverse=reverse)

def sort_by(values: Iterable[T], key: Callable[[T], T], reverse: bool = False) -> Iterable[T]:
    return sorted(values, key=lambda x: key(x), reverse=reverse)

def reverse(values: Iterable[T]) -> Iterable[T]:
    return reversed(list(values))

def foreach(values: Iterable[T], action: Callable[[T], None]) -> None:
    for x in values:
        action(x)

def anything(values: Iterable[T], predicate: Callable[[T], bool]) -> bool:
    return any(predicate(x) for x in values)

def every(values: Iterable[T], predicate: Callable[[T], bool]) -> bool:
    return all(predicate(x) for x in values)

def is_empty(values: Iterable[T]) -> bool:
    return sum(1 for _ in values) == 0

def to_list(values: Iterable[T]) -> List[T]:
    return list(values)

def to_set(values: Iterable[T]) -> set[T]:
    return set(values)
