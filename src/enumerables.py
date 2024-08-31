from collections.abc import Iterable
from typing import Callable, List
from itertools import islice, takewhile, dropwhile
from functools import reduce


class Enumerable[T: Iterable]:
    """
    The `Enumerable` class is  used to perform LINQ-like operations on a collection of values.
    """
    def __init__(self) -> None:
        self._values: Iterable[T] = []

    def of(self, values: Iterable[T]) -> 'Enumerable[T]':
        """
        The `of` method is used to create an Enumerable object from a collection of values.
        """
        self._values = values
        return self

    def empty(self) -> 'Enumerable[T]':
        """
        The `empty` method is used to create an empty Enumerable object.
        """
        return Enumerable().of([])

    def where(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        The `where` method is used to filter the values of the Enumerable object based on a predicate.
        """
        return Enumerable().of(filter(predicate, self._values))

    def select(self, selector: Callable[[T], T]) -> 'Enumerable[T]':
        """
        The `select` method is used to project the values of the Enumerable object based on a selector.
        """
        return Enumerable().of(map(selector, self._values))

    def select_many(self, selector: Callable[[T], Iterable[T]]) -> 'Enumerable[T]':
        """
        The `select_many` method flattens the values of the Enumerable object based on a selector.
        """
        return Enumerable().of(x for y in self._values for x in selector(y))

    def distinct(self) -> 'Enumerable[T]':
        """
        The `distinct` method is used to remove duplicate values from the Enumerable object.
        """
        seen = set()
        return Enumerable().of(x for x in self._values if x not in seen and not seen.add(x))

    def distinct_by(self, key_selector: Callable[[T], T]) -> 'Enumerable[T]':
        """
        The `distinct_by` method is used to remove duplicate values from the Enumerable object based on a key selector.
        """
        seen = set()
        return Enumerable().of(x for x in self._values if (key := key_selector(x)) not in seen and not seen.add(key))

    def take(self, count: int) -> 'Enumerable[T]':
        """
        The `take` method is used to take the first `count` values from the Enumerable object.
        """
        return Enumerable().of(islice(self._values, count))

    def take_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        The `take_while` method is used to take values from the Enumerable object while the predicate is true.
        """
        return Enumerable().of(takewhile(predicate, self._values))

    def skip(self, count: int) -> 'Enumerable[T]':
        """
        The `skip` method is used to skip the first `count` values from the Enumerable object.
        """
        return Enumerable().of(islice(self._values, count, None))

    def skip_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        The `skip_while` method is used to skip values from the Enumerable object while the predicate is true.
        """
        return Enumerable().of(dropwhile(predicate, self._values))

    def aggregate(self, func: Callable[[T, T], T]) -> T:
        """
        The `aggregate` method is used to apply an accumulator function over the values of the Enumerable object
        """
        return reduce(func, self._values)

    def aggregate_with_seed(self, func: Callable[[T, T], T], seed: T) -> T:
        """
        The `aggregate_with_seed` method is used to apply an accumulator function over the values of the Enumerable
        object with a seed/initial value.
        """
        return reduce(func, self._values, seed)

    def count(self) -> int:
        """
        The `count` method is used to count the number of values in the Enumerable object.
        """
        return sum(1 for _ in self._values)

    def count_where(self, predicate: Callable[[T], bool]) -> int:
        """
        The `count_where` method is used to count the number of values in the Enumerable object that satisfy a predicate.
        """
        return sum(1 for x in self._values if predicate(x))

    def concat(self, values: Iterable[T]) -> 'Enumerable[T]':
        """
        The `concat` method is used to concatenate the values of the Enumerable object with another collection of values.
        """
        return Enumerable().of(list(self._values) + list(values))

    def first(self) -> T:
        """
        The `first` method is used to get the first value of the Enumerable object. If the Enumerable object is empty,
        it returns `None`.
        """
        return next(iter(self._values), None)

    def first_where(self, predicate: Callable[[T], bool]) -> T:
        """
        The `first_where` method is used to get the first value of the Enumerable object that satisfies a predicate.
        """
        return next((x for x in self._values if predicate(x)), None)

    def last(self) -> T:
        """
        The `last` method is used to get the last value of the Enumerable object. If the Enumerable object is empty,
        it returns `None`.
        """
        return next(reversed(list(self._values)), None)

    def last_where(self, predicate: Callable[[T], bool]) -> T:
        """
        The `last_where` method is used to get the last value of the Enumerable object that satisfies a predicate.
        """
        return next(reversed([x for x in self._values if predicate(x)]), None)

    def sort(self, key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]':
        """
        The `sort` method is used to sort the values of the Enumerable object based on a key.
        """
        return Enumerable().of(sorted(self._values, key=key, reverse=reverse))

    def sort_by(self, key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]':
        """
        The `sort_by` method is used to sort the values of the Enumerable object based on a key.
        """
        return Enumerable().of(sorted(self._values, key=lambda x: key(x), reverse=reverse))

    def reverse(self) -> 'Enumerable[T]':
        """
        The `reverse` method is used to reverse the values of the Enumerable object
        """
        return Enumerable().of(reversed(list(self._values)))

    def foreach(self, action: Callable[[T], None]) -> None:
        """
        The `foreach` method is used to perform an action on each value of the Enumerable object.
        """
        for x in self._values:
            action(x)

    def any(self, predicate: Callable[[T], bool]) -> bool:
        """
        The `any` method is used to check if any value in the Enumerable object satisfies a predicate.
        """
        return any(predicate(x) for x in self._values)

    def all(self, predicate: Callable[[T], bool]) -> bool:
        """
        The `all` method is used to check if all values in the Enumerable object satisfy a predicate.
        """
        return all(predicate(x) for x in self._values)

    def is_empty(self) -> bool:
        """
        The `is_empty` method is used to check if the Enumerable object is empty.
        """
        return self.count() == 0

    def to_list(self) -> List[T]:
        """
        The `to_list` method is used to convert the Enumerable object to a list.
        """
        return list(self._values)

    def to_set(self) -> set[T]:
        """
        The `to_set` method is used to convert the Enumerable object to a set.
        """
        return set(self._values)

    def __next__(self) -> T:
        return next(iter(self._values)) if not self.is_empty() else None

    def __iter__(self) -> Iterable[T]:
        return iter(self._values)
