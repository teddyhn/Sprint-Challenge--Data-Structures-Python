from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity and self.current is not self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
        elif self.storage.length == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        while len(list_buffer_contents) < self.storage.length:
            list_buffer_contents.append(self.current.value)
            if self.current.next is not None:
                self.current = self.current.next
            else:
                self.current = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_index = 0
        self.storage = [0] * capacity

    def append(self, item):
        self.storage[self.current_index] = item
        self.current_index += 1

        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self):
        return [i for i in self.storage if i]
