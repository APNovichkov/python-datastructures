import os
import sys

from hashtable import HashTable


def get_word(jumble, ht):
    print(f"Trying to unjumble: {jumble}")

    print(ht.get("doctor"))

    pass

4
if __name__ == "__main__":
    print("Running word jumbler")
    jumble = sys.argv[1]
    print(f"Input jumble: {jumble}")

    dict_path = "/usr/share/dict/words"
    ht = HashTable()
    with open(dict_path, 'r') as f:
        for line in f:
            d_words.set(str(list(line).sort_values()), line)

    get_word(jumble, ht)
