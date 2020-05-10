def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    hashtable = {}

    for index, weight in enumerate(weights):
        diff = limit-weight
        if diff in hashtable:
            output = [hashtable[diff], index]
            output.sort(reverse=True)
            return (output)
        else:
            hashtable[weight] = index

    return None


# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)

# print(answer_3)
