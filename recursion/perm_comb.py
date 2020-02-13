import sys

def find_permutations(input, level):
    output_perms = []

    if len(input) == 1:
        print("--------------")
        print("In Level {}".format(level))
        print("Length is 1")
        print("Returning: {}".format(input))
        return input

    output_index = 0

    for index, item in enumerate(input):
        print("--------------")
        print("In Level {}".format(level))
        print("Current array {}".format(input))
        print("In item: {}".format(item))
        new_array = input[:index] + input[index + 1:]
        print("new array: {}".format(new_array))
        # print("old array: {}".format(input))

        perms = find_permutations(new_array, level + 1)

        for perm in perms:
            output_perms.append("")
            print("--------------")
            print("In Level {}".format(level))
            print("Adding perms {} to {}".format(perm, output_perms[output_index]))
            output_perms[output_index] = output_perms[output_index] + perm
            output_index += 1
            print("Output Perms: {}".format(output_perms))

    return output_perms


if __name__ == "__main__":
    input = sys.argv[1]
    print(f'Finding all permutations for: {input}')

    perms = find_permutations(list(input), 0)
    print(perms)
