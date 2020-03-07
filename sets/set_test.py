from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_add(self):
        set = Set()
        set.add('A')
        set.add('B')
        set.add('C')
        assert set.contains('A') is True
        assert set.contains('B') is True
        assert set.contains('C') is True
        assert set.size() == 3

    def test_contains(self):
        set = Set()
        set.add('A')
        set.add('B')
        assert set.contains('D') is False
        assert set.contains('B') is True

    def test_remove(self):
        set = Set()
        set.add('A')
        set.add('B')

        assert set.size() == 2

        set.remove('B')
        assert set.contains('B') is False
        assert set.size() == 1

    def test_size(self):
        set = Set()
        set.add('A')
        set.add('B')

        assert set.size() == 2

        set.add('C')
        assert set.size() == 3

        set.remove('A')
        assert set.size() == 2

    def test_union(self):
        set1 = Set()
        set1.add('A')
        set1.add('B')

        set2 = Set()
        set2.add('B')
        set2.add('C')

        assert set1.union(set2).size() == 3
        assert set1.union(set2).contains('C') is True

    def test_intersection(self):
        set1 = Set()
        set1.add('A')
        set1.add('B')

        set2 = Set()
        set2.add('B')
        set2.add('C')

        assert set1.intersection(set2).size() == 1
        assert set1.intersection(set2).contains('B') is True
        assert set1.intersection(set2).contains('A') is False

    def test_difference(self):
        set1 = Set()
        set1.add('A')
        set1.add('B')

        set2 = Set()
        set2.add('B')
        set2.add('C')

        assert set1.difference(set2).size() == 1
        assert set1.difference(set2).contains('A') is True
        assert set1.difference(set2).contains('B') is False

    def test_is_subset(self):
        set1 = Set()
        set1.add('A')
        set1.add('B')

        set2 = Set()
        set2.add('A')
        set2.add('B')
        set2.add('C')

        assert set1.is_subset(set2) is True
        assert set2.is_subset(set1) is False
