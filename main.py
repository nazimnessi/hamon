from collections import Counter
from typing import Iterable, Dict, Any


def count_elements(data: Iterable[Any]) -> Dict[Any, int]:
    """
    Counts the frequency of each unique element in the iterable `data`.

    Args:
        data (Iterable[Any]): An iterable (e.g., string, list, tuple) whose elements are to be counted.

    Returns:
        Dict[Any, int]: A dictionary where keys are elements from `data` and values are their counts.

    Raises:
        TypeError: If the input `data` is not an iterable.
    """
    if not isinstance(data, (str, list, tuple)):
        raise TypeError(
            "Input must be an iterable like a string, list, or tuple.")

    return dict(Counter(data))


count_elements("hello world")
