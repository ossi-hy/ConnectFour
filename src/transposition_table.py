from collections import OrderedDict

class TranspositionTable(OrderedDict):
    def __init__(self, size=128, *args, **kwargs):
        self.size = size
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value) -> None:
        super().__setitem__(key, value)
        if len(self) > self.size:
            oldest = next(iter(self))
            del self[oldest]


