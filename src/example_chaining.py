from enumerables import Enumerable

def factorial(n: int) -> int: return 1 if n == 0 else n * factorial(n - 1)

result: int = (
    Enumerable().of(range(10))
    .select(factorial)
    .where(lambda x: x % 2 == 0)
    .aggregate(lambda x, y: x + y)
)

print(result)