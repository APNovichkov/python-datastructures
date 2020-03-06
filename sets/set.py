from hashtable import HashTable

class Set(object):

    default_val = None

    def __init__(self, items=None):
        self.ht = HashTable()

        if items is not None:
            for item in items:
                self.ht.set(item, Set.default_val)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = [f"{key}" for key in self.ht.keys()]
        return f"Set: {', '.join(items)}"

    def contains(self, item):
        return self.ht.contains(item)

    def add(self, item):
        self.ht.set(item, Set.default_val)

    def remove(self, item):
        self.ht.delete(item)

    def size(self):
        return self.ht.length()

    def union(self, input_set):
        """Return another set which is the union of self and input set"""
        output_set = Set(self.ht.keys())
        for item in input_set.ht.keys():
            output_set.add(item)
        return output_set

    def intersection(self, input_set):
        """Return another set which is the intersection of self and input set"""

        output_set = Set(self.ht.keys())
        other_set = input_set

        # Choose the smaller set
        if input_set.size() < self.size():
            output_set = input_set
            other_set = self

        for item in output_set.ht.keys():
            if not other_set.contains(item):
                output_set.remove(item)

        return output_set

    def difference(self, input_set):
        """Find the difference of self and input set"""

        output_set = Set()
        for item in self.ht.keys():
            if not input_set.contains(item):
                output_set.add(item)
        return output_set

    def is_subset(self, input_set):
        """Return true if self is subset of input_set, false if not

        Best Case: O(1)
        Worst Case: O(n) where n is # items in self
        """

        # If self is larger than input set, self can't be subset of input_set
        if self.size() > input_set.size():
            return False

        for item in self.ht.keys():
            if not input_set.contains(item):
                # Found at least one item not in self
                return False
        return True


if __name__ == "__main__":
    s1 = Set()
    s1.add("a")
    s1.add("b")
    s1.add("c")
    s1.add("d")
    print(s1)
    s1.remove("a")
    print(s1)
    s1.remove("d")
    print(s1)
    print(f"Does s1 contain 'b'? -> {s1.contains('b')}")
    print(f"Does s1 contain 'd'? -> {s1.contains('d')}")

    print("\nNow let's check union, intersection, difference and is_subset methods")
    s1 = Set()
    s1.add("a")
    s1.add("b")
    s1.add("c")
    s1.add("d")
    print(f"Set 1: {s1}")

    s2 = Set()
    s2.add("c")
    s2.add("d")
    s2.add("e")
    s2.add("f")
    print(f"Set 2: {s2}\n")

    print(f"Union of set 1 and 2 is: {s1.union(s2)}")
    print(f"Intersection of set 1 and 2 is: {s1.intersection(s2)}")
    print(f"Difference of set 1 and 2 is: {s1.difference(s2)}")
    print(f"Is set1 a subset of s2? -> {s1.is_subset(s2)}")
