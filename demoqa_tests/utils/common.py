from typing import Iterable, Any


def flatten(nested_iterable: Iterable[Iterable[Any]]):
    return tuple(item for nested in nested_iterable for item in nested)
