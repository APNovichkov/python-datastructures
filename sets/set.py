from abstract_data_types.hashtable import HashTable

class Set(Object):

    ht = HashTable()
    d_val = "value"

    def __init__(self, items=None):
        if items is not None:
            for item in items:
                self.ht.set(item, d_val)

    def contains(self, item):
        print(f"Checking if ht contains: {item}")
        return self.ht.contains(item)

    def add(self, item):
        print(f"Adding item: {item}")
        self.ht.set(item, self.d_val)

    def remove(self, item):
        print(f"Removing item: {item}")
        self.ht.delete(item)

    def union(self, input_set):
        output_set = self(self.ht.keys())
        for item in input_set:
            output_set.add(item)
        return output_set

    def intersection(self, input_set):
        output_set = self()
        for item in ht.keys():
            if item in input_set.keys():
                output_set.add(item)
        return output_set

    def difference(self, input_set):
        output_set = self()
        for item in ht.keys():
            if item not in input_set.keys():
                output_set.add(item)
        return output_set

    def is_subset(self, input_set):
        for item in ht.keys():
            if item not in input_set.keys():
                return False
        return True
