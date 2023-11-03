from utils import memoize
from pprint import pprint

class MyClass:

    def __init__(self) -> None:
        self.sums = {}

    @memoize
    def a_method(self):
        print("a_method called")
        return 42

    @memoize
    def add(self, *args):
        result = sum(args)
        self.sums.update({f"({args})": result})
        pprint(self.sums)
        return result
