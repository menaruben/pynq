from collections.abc import Iterable
from types import UnionType
from typing import Any, Callable, List, Tuple
from enumerable_funcs import *
from functools import singledispatch, singledispatchmethod


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
        return Enumerable().of(where(self._values, predicate))
    
    def select(self, selector: Callable[[T], T]) -> 'Enumerable[T]':
        """
        The `select` method is used to project the values of the Enumerable object based on a selector.
        """
        return Enumerable().of(select(self._values, selector))
    
    def select_many(self, selector: Callable[[T], Iterable[T]]) -> 'Enumerable[T]':
        """
        The `select_many` method flattens the values of the Enumerable object based on a selector.
        """
        return Enumerable().of(select_many(self._values, selector))
    
    def distinct(self) -> 'Enumerable[T]':
        """
        The `distinct` method is used to remove duplicate values from the Enumerable object.
        """
        seen = set()
        return Enumerable().of(distinct(self._values))
    
    def distinct_by(self, key_selector: Callable[[T], T]) -> 'Enumerable[T]':
        """
        The `distinct_by` method is used to remove duplicate values from the Enumerable object based on a key selector.
        """
        return Enumerable().of(distinct_by(self._values, key_selector))
    
    def take(self, count: int) -> 'Enumerable[T]':
        """
        The `take` method is used to take the first `count` values from the Enumerable object.
        """
        return Enumerable().of(take(self._values, count))

    def take_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        The `take_while` method is used to take values from the Enumerable object while the predicate is true.
        """
        return Enumerable().of(take_while(self._values, predicate))
    
    def skip(self, count: int) -> 'Enumerable[T]':
        """
        The `skip` method is used to skip the first `count` values from the Enumerable object.
        """
        return Enumerable().of(skip(self._values, count))
    
    def skip_while(self, predicate: Callable[[T], bool]) -> 'Enumerable[T]':
        """
        The `skip_while` method is used to skip values from the Enumerable object while the predicate is true.
        """
        return Enumerable().of(skip_while(self._values, predicate))
    
    def aggregate(self, func: Callable[[T, T], T]) -> T:
        """
        The `aggregate` method is used to apply an accumulator function over the values of the Enumerable object
        """
        return aggregate(self._values, func)
    
    def aggregate_with_seed(self, func: Callable[[T, T], T], seed: T) -> T:
        """
        The `aggregate_with_seed` method is used to apply an accumulator function over the values of the Enumerable
        object with a seed/initial value.
        """
        return aggregate_with_seed(self._values, func, seed)
    
    def count(self) -> int:
        """
        The `count` method is used to count the number of values in the Enumerable object.
        """
        return count(self._values)
    
    def count_where(self, predicate: Callable[[T], bool]) -> int:
        """
        The `count_where` method is used to count the number of values in the Enumerable object that satisfy a predicate.
        """
        return count_where(self._values, predicate)
    
    def concat(self, values: Iterable[T]) -> 'Enumerable[T]':
        """
        The `concat` method is used to concatenate the values of the Enumerable object with another collection of values.
        """
        return Enumerable().of(concat(self._values, values))
    
    def first(self) -> T:
        """
        The `first` method is used to get the first value of the Enumerable object. If the Enumerable object is empty,
        it returns `None`.
        """
        return first(self._values)
    
    def first_where(self, predicate: Callable[[T], bool]) -> T:
        """
        The `first_where` method is used to get the first value of the Enumerable object that satisfies a predicate.
        """
        return first_where(self._values, predicate)
    
    def last(self) -> T:
        """
        The `last` method is used to get the last value of the Enumerable object. If the Enumerable object is empty,
        it returns `None`.
        """
        return last(self._values)
    
    def last_where(self, predicate: Callable[[T], bool]) -> T:
        """
        The `last_where` method is used to get the last value of the Enumerable object that satisfies a predicate.
        """
        return last_where(self._values, predicate)
    
    def sort(self, key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]':
        """
        The `sort` method is used to sort the values of the Enumerable object based on a key.
        """
        return Enumerable().of(sort(self._values, key=key, reverse=reverse))
    
    def sort_by(self, key: Callable[[T], T], reverse: bool = False) -> 'Enumerable[T]':
        """
        The `sort_by` method is used to sort the values of the Enumerable object based on a key.
        """
        return Enumerable().of(sort_by(self._values, key=key, reverse=reverse))
    
    def reverse(self) -> 'Enumerable[T]':
        """
        The `reverse` method is used to reverse the values of the Enumerable object
        """
        return Enumerable().of(reverse(self._values))
    
    def foreach(self, action: Callable[[T], None]) -> None:
        """
        The `foreach` method is used to perform an action on each value of the Enumerable object.
        """
        foreach(self._values, action)
    
    def any(self, predicate: Callable[[T], bool]) -> bool:
        """
        The `anything` method is used to check if any value in the Enumerable object satisfies a predicate.
        """
        return anything(self._values, predicate)
    
    def all(self, predicate: Callable[[T], bool]) -> bool:
        """
        The `every` method is used to check if all values in the Enumerable object satisfy a predicate.
        """
        return every(self._values, predicate)
    
    def is_empty(self) -> bool:
        """
        The `is_empty` method is used to check if the Enumerable object is empty.
        """
        return is_empty(self._values)
    
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

    def combine(self, other: 'Enumerable[T]') -> 'Enumerable[T]':
        """
        The `combine` method is used to combine this Enumerable object with another Enumerable object.
        """
        return Enumerable().of(concat(self._values, other.to_list()))
    
    def zip(self, other: 'Enumerable[T]') -> 'Enumerable[Tuple[T, T]]':
        """
        The `zip` method is used to zip this Enumerable object with another Enumerable object
        to create a new Enumerable object of tuples.
        """
        return Enumerable().of(zip(self._values, list(other)))

    def __or__(self, func: Callable) -> UnionType:
        if isinstance(func, Predicate):
            return self.where(func)
        elif isinstance(func, Selector):
            return self.select(func)
        elif isinstance(func, Accumulator):
            return self.aggregate(func)
        elif isinstance(func, Action):
            return self.foreach(func)
        else:
            return func(self)

    def __next__(self) -> T:
        return next(iter(self._values)) if not self.is_empty() else None

    def __iter__(self) -> Iterable[T]:
        return iter(self._values)
