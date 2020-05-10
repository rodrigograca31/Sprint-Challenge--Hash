def intersection(arrays):
    """
    YOUR CODE HERE
    """

    result = []
    hashtable = {}

    for array in arrays:
        for item in array:
            # print(item)
            if item in hashtable:
                hashtable[item] += 1
            else:
                hashtable[item] = 1

    for index, number in enumerate(hashtable):
        # print(hashtable[number])
        if hashtable[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(20, 30)) + [1, 2, 3])

    print(intersection(arrays))


# result = []
#    hashtable = {}
#     print(arrays)
#     arrays.sort(reverse=True)
#     print(arrays)

#     # for array in arrays:
#     for item2 in arrays[0]:
#         print(item2)
#         for array in arrays[1:]:
#             print(array)
#             for item in array:
#                 if item == item2:
#                     # if item2 in hashtable:
#                     hashtable[item] += 1
#                 else:
#                     hashtable[item] = 1
