def has_negatives(a):
    """
    YOUR CODE HERE
    """

    hashtable = {}
    result = []

    for index, number in enumerate(a):
        # opposite = -number

        if -number in hashtable:
            result.append(abs(number))

        hashtable[number] = number

    return result


if __name__ == "__main__":
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    # print()
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
