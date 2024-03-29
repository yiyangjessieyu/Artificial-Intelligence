import math


def knn_predict(input, examples, distance, combine, k):

    example_input_output_distance = []
    for example_input, examples_output in examples:
        example_input_output_distance.append(
            {
                'example_input': example_input,
                'examples_output': examples_output,
                'distance': distance(input, example_input)
            }
        )

    example_input_output_distance.sort(key=get_distance)

    neighbor_outputs = [neighbor_dict['examples_output'] for neighbor_dict in example_input_output_distance[:k]]

    farthest_selected = example_input_output_distance[k-1]['distance']
    neighbor_outputs += [nearest_unselected_dict['examples_output']
                         for nearest_unselected_dict in example_input_output_distance[k:]
                         if nearest_unselected_dict['distance'] == farthest_selected]

    output = combine(neighbor_outputs)
    return output


# custom functions to get employee info
def get_distance(example):
    return example.get('distance')


def euclidean_distance(v1, v2):
    return math.sqrt(sum((v1[i] - v2[i]) ** 2 for i in range(len(v1))))


def majority_element(labels):
    count_dict = dict.fromkeys(labels, 0)
    for item in labels:
        count_dict[item] += 1
    max_count = count_dict[max(count_dict, key=count_dict.get)]

    max_labels = [label for label, count in count_dict.items() if max_count == count]
    max_labels.sort()

    return max_labels[0]


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
