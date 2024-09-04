from typing import Iterable, Callable, TypeVar, List
from itertools import islice, takewhile, dropwhile
from functools import reduce

class Func[T, U]:
    def __init__(self, func: Callable[[T], U]) -> None:
        self.func = func

    def __call__(self, x: T) -> U:
        return self.func(x)


class Predicate[T](Func[T, bool]):
    def __init__(self, func: Callable[[T], bool]) -> None:
        self.func = func

    def __call__(self, x: T) -> bool:
        return self.func(x)


class Selector[T, U](Func[T, U]):
    def __init__(self, func: Callable[[T], U]) -> None:
        self.func = func

    def __call__(self, x: T) -> U:
        return self.func(x)


class Action[T](Func[T, None]):
    def __init__(self, func: Callable[[T], None]) -> None:
        self.func = func

    def __call__(self, x: T) -> None:
        self.func(x)

class Accumulator[T](Func[T, T]):
    def __init__(self, func: Callable[[T, T], T]) -> None:
        self.func = func

    def __call__(self, x: T, y: T) -> T:
        return self.func(x, y)

T = TypeVar('T')
U = TypeVar('U')

def where(values: Iterable[T], predicate: Predicate[T]) -> Iterable[T]:
    return filter(predicate, values)

def select(values: Iterable[T], selector: Selector[T, U]) -> Iterable[U]:
    return map(selector, values)

def select_many(values: Iterable[T], selector: Selector[T, Iterable[U]]) -> Iterable[U]:
    return (x for y in values for x in selector(y))

def distinct(values: Iterable[T]) -> Iterable[T]:
    seen = set()
    return (x for x in values if x not in seen and not seen.add(x))

def distinct_by(values: Iterable[T], key_selector: Selector[T, U]) -> Iterable[U]:
    seen = set()
    return (x for x in values if (key := key_selector(x)) not in seen and not seen.add(key))

def take(values: Iterable[T], count: int) -> Iterable[T]:
    return islice(values, count)

def take_while(values: Iterable[T], predicate: Predicate[T]) -> Iterable[T]:
    return takewhile(predicate, values)

def skip(values: Iterable[T], count: int) -> Iterable[T]:
    return islice(values, count, None)

def skip_while(values: Iterable[T], predicate: Predicate[T]) -> Iterable[T]:
    return dropwhile(predicate, values)

def aggregate(values: Iterable[T], func: Accumulator[T]) -> T:
    return reduce(func, values)

def aggregate_with_seed(values: Iterable[T], func: Accumulator[T], seed: T) -> T:
    return reduce(func, values, seed)

def count(values: Iterable[T]) -> int:
    return sum(1 for _ in values)

def count_where(values: Iterable[T], predicate: Predicate[T]) -> int:
    return sum(1 for x in values if predicate(x))

def concat(values: Iterable[T], other_values: Iterable[T]) -> Iterable[T]:
    return list(values) + list(other_values)

def first(values: Iterable[T]) -> T:
    return next(iter(values), None)

def first_where(values: Iterable[T], predicate: Predicate[T]) -> T:
    return next((x for x in values if predicate(x)), None)

def last(values: Iterable[T]) -> T:
    return next(reversed(list(values)), None)

def last_where(values: Iterable[T], predicate: Predicate[T]) -> T:
    return next(reversed([x for x in values if predicate(x)]), None)

def sort(values: Iterable[T], key: Selector[T, U], reverse: bool = False) -> Iterable[T]:
    return sorted(values, key=key, reverse=reverse)

def sort_by(values: Iterable[T], key: Selector[T, U], reverse: bool = False) -> Iterable[T]:
    return sorted(values, key=lambda x: key(x), reverse=reverse)

def reverse(values: Iterable[T]) -> Iterable[T]:
    return reversed(list(values))

def foreach(values: Iterable[T], action: Action[T]) -> None:
    [action(x) for x in values]

def intersect(values: Iterable[T], other_values: Iterable[T]) -> Iterable[T]:
    return (x for x in values if x in other_values)

def without(values: Iterable[T], other_values: Iterable[T]) -> Iterable[T]:
    return (x for x in values if x not in other_values)

def anything(values: Iterable[T], predicate: Predicate[T]) -> bool:
    return any(predicate(x) for x in values)

def every(values: Iterable[T], predicate: Predicate[T]) -> bool:
    return all(predicate(x) for x in values)

def is_empty(values: Iterable[T]) -> bool:
    return sum(1 for _ in values) == 0

def to_list(values: Iterable[T]) -> List[T]:
    return list(values)

def to_set(values: Iterable[T]) -> set[T]:
    return set(values)


