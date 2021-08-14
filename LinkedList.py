class Node:
    def __init__(self, value: int, next_: 'Node' = None):
        self._value = value
        self._next = next_

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_: int):
        self._value = value_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node: 'Node'):
        self._next = node


class LinkedList:
    def __init__(self):
        self._head = None

    def print(self):
        pass

    def add_front(self, value: int):
        pass

    def add_back(self, value: int):
        pass

    def insert_at(self, value: int, index: int):
        pass

    def remove_front(self) -> int:
        pass

    def remove_back(self) -> int:
        pass

    def remove_at(self, index: int) -> int:
        pass

    def remove_by_value(self, value: int):
        pass

    @property
    def length(self) -> int:
        pass

    def reverse(self):
        pass

    def intersection_sort(self):
        pass

    def merge_sort(self):
        pass
