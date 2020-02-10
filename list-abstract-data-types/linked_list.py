#!python

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes

        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        result = []  # Constant time to create a new list
        node = self.head  # Constant time to assign a variable reference

        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            result.append(node.data)  # Constant time to append to a list
            node = node.next  # Constant time to reassign a variable
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        node_count = 0
        node = self.head

        while node is not None:
            node_count += 1
            node = node.next

        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node = self.head

        for i in range(0, index):
            node = node.next

        return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        if index == 0:
            self.prepend(item)
            return

        if index == self.size:
            self.append(item)
            return

        c_node = self.head
        p_node = c_node
        new_node = Node(item)

        for i in range(0, index):
            p_node = c_node
            c_node = c_node.next

        p_node.next = new_node
        new_node.next = c_node
        self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head

        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""

        node = self.head  # Constant time to assign a variable reference
        while node is not None:  # Up to n iterations if we don't exit early
            if quality(node.data):  # Constant time to call quality function
                return node.data  # Constant time to return data

            node = node.next  # Constant time to reassign a variable

        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return new_item

            node = node.next

        raise ValueError("Item {} not found!".format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        node = self.head
        previous = None
        found = False

        while not found and node is not None:
            if node.data == item:
                found = True
            else:
                previous = node
                node = node.next

        if found:
            if node is not self.head and node is not self.tail:
                previous.next = node.next
                node.next = None

            if node is self.head:
                self.head = node.next
                node.next = None

            if node is self.tail:
                if previous is not None:
                    previous.next = None

                self.tail = previous

            self.size -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print("Insert item at index 1")
    ll.insert_at_index(1, 'D')
    print(ll)

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
