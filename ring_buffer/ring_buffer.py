from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # pass
        # using recursion
        # From README: When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
        # if storage is not full, add to tail and updated the current
        # if storage is full, remove the head(oldest) to free up space, add item to tail(newest)
            # if current is at the head, set the current to tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set the start to current and append value to contents
        # loop through the nodes and append values
            # if start.next, set nextItem to start next, else set nextItem to storage head
            # while nextItem does not equal start, append nextItem value to contents
                # if nextItem then set nextItem to nextItem next, else nextItem to storage head
            # return contents

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
