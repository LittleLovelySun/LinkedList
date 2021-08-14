from typing import Optional


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
        self._head: Optional[Node] = None
        self._length = 0

    @property
    def is_empty(self) -> bool:
        return self._head is None

    def print(self):
        if self.is_empty:
            print('List is empty.')
            return

        print('List: ', end='')

        current = self._head
        while current:
            print(current.value, end=' ' if current.next else '\n')
            current = current.next

    def add_front(self, value: int):
        inserted = Node(value, self._head)
        self._head = inserted
        self._length += 1

    def add_back(self, value: int):
        self._length += 1
        if not self._head:
            self._head = Node(value)
            return

        current = self._head
        while current.next:
            current = current.next

        current.next = Node(value)

    def insert_at(self, value: int, index: int):
        if index < 0 or index > self.length:
            raise IndexError(f'cannot insert `{value}` at `{index}` index: out of range')

        self._length += 1

        if index == 0:
            self.add_front(value)
            return

        prev = self._head
        for _ in range(index - 1):
            prev = prev.next

        inserted = Node(value, prev.next)
        prev.next = inserted

    def remove_front(self) -> int:
        if self.is_empty:
            raise IndexError('cannot remove front (list is empty)')

        self._length -= 1

        front_value = self._head.value
        self._head = self._head.next
        return front_value

    def remove_back(self) -> int:
        if self.is_empty:
            raise IndexError('Cannot remove front (list is empty)')

        self._length -= 1

        prev = self._head
        current = self._head

        while current.next is not None:
            prev = current
            current = current.next

        back_value = current.value
        if current == self._head:
            self._head = None
        else:
            prev.next = None
        return back_value

    def remove_at(self, index: int) -> int:
        if index < 0 or index >= self.length:
            raise IndexError(f'cannot insert at `{index}` index: out of range')

        self._length -= 1

        prev = self._head
        for _ in range(index - 1):
            prev = prev.next

        if prev == self._head:
            remove_value = self._head.value
            self._head = prev.next
        else:
            remove_value = prev.next.value
            prev.next = prev.next.next

        return remove_value

    def remove_by_value(self, value: int):
        prev = self._head
        current = self._head

        while current:
            if current.value == value:
                if current == self._head:
                    self._head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current

            current = current.next

    @property
    def length(self) -> int:
        return self._length

    def reverse(self):
        current = self._head
        self._head = None

        while current:
            tmp = current
            current = current.next
            tmp.next = self._head
            self._head = tmp

    def intersection_sort(self):
        pass

    def merge_sort(self):
        pass
