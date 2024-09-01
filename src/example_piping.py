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
