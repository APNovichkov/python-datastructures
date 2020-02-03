#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return True

    started_matching = False
    pattern_index = 0
    text_first_matched_index = 0
    loop_index = 0

    while loop_index < len(text):
        # If chars match
        if text[loop_index] == pattern[pattern_index]:
            # Edge case for if you are matching one letter
            if pattern_index == len(pattern) - 1:
                return True

            if not started_matching:
                # If first started looking
                text_first_matched_index = loop_index
                started_matching = True
                pattern_index += 1
                loop_index += 1

            else:
                # If found full pattern return True
                if pattern_index == len(pattern) - 1:
                    return True

                pattern_index += 1
                loop_index += 1

        else:
            if started_matching:
                started_matching = False
                pattern_index = 0
                loop_index = text_first_matched_index

            loop_index += 1

    # Return if match not found
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""

    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return 0

    started_matching = False
    pattern_index = 0
    text_first_matched_index = 0
    loop_index = 0

    while loop_index < len(text):
        # If chars match
        if text[loop_index] == pattern[pattern_index]:
            # If we have a first match
            if not started_matching:
                # Edge case for if we are checking only one letter
                if pattern_index == len(pattern) - 1:
                    return loop_index

                text_first_matched_index = loop_index
                started_matching = True
                pattern_index += 1
                loop_index += 1

            else:
                # If found full pattern return the index of that match
                if pattern_index == len(pattern) - 1:
                    return text_first_matched_index

                pattern_index += 1
                loop_index += 1

        else:
            if started_matching:
                started_matching = False
                pattern_index = 0
                loop_index = text_first_matched_index

            loop_index += 1

    # Return if match not found
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""

    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return list(range(0, len(text)))

    started_matching = False
    pattern_index = 0
    text_first_matched_index = 0
    loop_index = 0

    output_index_list = []

    while loop_index < len(text):
        # If chars match
        if text[loop_index] == pattern[pattern_index]:
            # If we have a first match
            if not started_matching:
                # This is needed if pattern only contains one char
                if len(pattern) == 1:
                    output_index_list.append(loop_index)
                    loop_index += 1
                # Do this if pattern is more than one
                else:
                    text_first_matched_index = loop_index
                    started_matching = True
                    pattern_index += 1
                    loop_index += 1

            # Do this if we have not already started matching
            else:
                # If found full pattern return the index of that match
                if pattern_index == len(pattern) - 1:
                    output_index_list.append(text_first_matched_index)
                    loop_index = text_first_matched_index + 1

                    # Reset values
                    pattern_index = 0
                    text_first_matched_index = None
                    started_matching = False
                else:
                    # Increment values
                    pattern_index += 1
                    loop_index += 1

        # If chars don't match
        else:
            # If we were already looking
            if started_matching:
                started_matching = False
                pattern_index = 0
                loop_index = text_first_matched_index

            loop_index += 1

    # Return if match not found
    return output_index_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))

    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))

    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
