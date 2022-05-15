from __future__ import annotations
from collections import OrderedDict
from typing import Any

class TranspositionTable(OrderedDict):
    def __init__(self, size=128, *args, **kwargs):
        self.size = size
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: Any) -> Any:
        """Get item from the transposition table and move it to the end

        Args:
            key (Any): key for the value

        Returns:
            Any: stored value
        """
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key: Any, value: Any) -> None:
        """Add item to the transposition table. If full remove least recently added/gotten item.

        Args:
            key (Any): key for the value
            value (Any): value to be stored
        """
        super().__setitem__(key, value)
        if len(self) > self.size:
            oldest = next(iter(self))
            del self[oldest]


