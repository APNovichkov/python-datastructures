import sys
from log_it import logit

from hashtable import HashTable

def unjumble_words(jumble):
    # Get max length of input words
    max_jumble_length = 0
    for word in jumble:
        max_jumble_length = max(max_jumble_length, len(word))

    # Build hashtable of dictionary words
    dict_path = "/usr/share/dict/words"
    ht = build_ht(dict_path, max_jumble_length)

    # Run through each input jumble, and unjumble it
    for word in jumble:
        word = word.lower()
        logit.log(f"Input jumbled word: {word}")
        jumble = _sort_word(word)
        logit.log(f"Input jumbled word sorted: {word}")

        get_word(jumble, ht)

def get_word(jumble, ht):
    """Unjumble the input jumble."""

    logit.log(f"Trying to unjumble: {jumble}")

    # Since we sorted both the input jumble and all the words in the hashtable, we can just match exactly
    # and if there is a match, we can get the real word from the hashtable, and if there isnt,
    # then we say we could not unjumble it

    if ht.contains(jumble):
        logit.log(f"Successfuly unjumbled word! -> {ht.get(jumble)}", logit.SUCCESS)
    else:
        logit.log(f"Unfortunatenly I could not unjumble this word for you: {jumble}", logit.ERROR)

def build_ht(word_list_fp, jumble_length):
    """Build hashtable of words sorted by character whose total length is less than or equal to the largest input jumbled word"""
    ht = HashTable()

    # Run through it the whole list
    logit.log(f'Building hashtable for words at path: {word_list_fp}')
    with open(word_list_fp, 'r') as f:
        for line in f:
            word = line.strip().lower()
            # Only add words to hashtable if they are of the same length as jumbled word
            if len(word) == jumble_length:
                # Sort the key by character
                key = _sort_word(word)
                value = word
                # Add word to the hashtable
                ht.set(key, value)

    logit.log('Done building hashtable for dictionary words', logit.SUCCESS)
    return ht

def _sort_word(word):
    word = list(word)
    word.sort()
    word = _char_arr_to_str(word)
    return word

def _char_arr_to_str(array):
    return ''.join(array)


if __name__ == "__main__":
    """Run word de-jumbler from CLI"""

    logit.log("Running word jumbler")

    jumble = sys.argv[1:]

    # Run app
    unjumble_words(jumble)
