'''
Poits and Segments

Quick sorting practice
'''

from typing import List, Tuple


Pair = Tuple[int, int]


def read_pair() -> Pair:
    '''Reads pair of int numbers from stdin line'''

    pair_list = tuple(int(n) for n in input().split())

    if len(pair_list) != 2:
        raise Exception('Unexpected Pair length')

    return pair_list

def read_data() -> Tuple[List[Pair], List[Pair]]:
    '''
    Reads input data from stdin by lines:
        - number of segments (n) and number of dots (m);
        - n lines of segments coordinates;
        - line with m dots

    Returns tuple of:
        - list of segments
        - list of dots
    '''

    number_of_segments, number_of_dots = read_pair()

    print('number_of_segments:', number_of_segments)
    print('number_of_dots:', number_of_dots)

    segments_list = [read_pair() for _ in range(number_of_segments)]

    print('segments_list:', segments_list)

    dots_coordinates_list = [int(n) for n in input().split()]
    fact_number_of_dots = len(dots_coordinates_list)
    if fact_number_of_dots != number_of_dots:
        raise Exception(
            f'Unexpected number of dots; expected: {number_of_dots}; fact: {fact_number_of_dots}')

    print('dots_coordinates_list:', dots_coordinates_list)

    return segments_list, dots_coordinates_list

def count_dots_in_segments(segments_list, dots_coordinates_list):
    '''
    Counts the number of segments that contain points

    Returns the list of intersections numbers
    '''

    dots_in_segments_count_list = []

    for dot_coordinate in dots_coordinates_list:
        dot_in_segments_count = 0
        for segment in segments_list:
            if segment[0] <= dot_coordinate <= segment[1]:
                dot_in_segments_count += 1

        dots_in_segments_count_list.append(dot_in_segments_count)

    return dots_in_segments_count_list

def quick_sort(source_list, comparison_function):
    '''
    Sorting list elements using comparison function

    Comparison function is expected to return:
     -  0 - elements are equal;
     - -1 - first element is less then second;
     -  1 - first element is greater then second.
    '''

    pass


if __name__ == '__main__':
    # input_segments_list, input_dots_list = read_data()
    input_segments_list = [[1, 4], [98, 100], [3, 6], [3, 12], [-2, 8], [0, 4]]
    input_dots_list = [10, 3, 100, 5, 90]

    print(enumerate(input_dots_list))

    for i, n in enumerate(input_dots_list):
        print(i, n)

    list_of_intersections = count_dots_in_segments(input_segments_list, input_dots_list)

    print(*list_of_intersections)
