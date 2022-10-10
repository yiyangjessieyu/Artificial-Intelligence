import math


def knn_predict(input, examples, distance, combine, k):
    distances = [euclidean_distance([input][0], pair[0]) for pair in examples]
    print(distances)
    neighbor_pair = [examples[i] for i, distance in enumerate(distances) if input[0] - distance <= k]
    neighbor_values = [examples[i][1] for i, distance in enumerate(distances) if input[0] - distance <= k]
    print(neighbor_pair)
    if input == [4]:
        print(distances, neighbor_values)
    output = majority_element(neighbor_values)
    return output


def euclidean_distance(v1, v2):
    return math.sqrt(sum((v1[i] - v2[i]) ** 2 for i in range(len(v1))))


def majority_element(labels):
    count_dict = dict.fromkeys(labels, 0)
    for item in labels:
        count_dict[item] += 1
    max_count = count_dict[max(count_dict, key=count_dict.get)]

    max_labels = [label for label, count in count_dict.items() if max_count == count]

    return max_labels[-1]



def main():
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()

    # using knn for predicting numeric values

    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]

    def average(values):
        return sum(values) / len(values)

    distance = euclidean_distance
    combine = average

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()


if __name__ == "__main__":
    main()
