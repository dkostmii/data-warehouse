from typing import TypeVar, Generic, Protocol

T = TypeVar("T")

class UniqueGeneratorException(Exception):
    pass

class Generator(Generic[T], Protocol):
    def get(self, *args, **kwargs) -> T:
        ...

class UniqueGenerator(Generic[T]):
    _history: list[T]
    unique_max_iter: int

    def __init__(self, gen: Generator[T], unique_max_iter: int = 2):
        self._gen = gen
        self.unique_max_iter = unique_max_iter
        self._history = []

    def get_unique(self, *args, **kwargs) -> T:
        unique_iter = 0
        result = self._gen.get(*args, **kwargs)

        while result in self._history and unique_iter < self.unique_max_iter:
            unique_iter += 1
            result = self._gen.get(*args, **kwargs)

        if result in self._history:
            raise UniqueGeneratorException(f"Cannot generate unique value. Reached unique_max_iter={unique_iter}. Current value: {result}.")

        self._history.append(result)
        return result