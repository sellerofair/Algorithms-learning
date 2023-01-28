'''
Poits and Segments

Quick sorting practice
'''

from typing import List, Tuple


def read_int_list() -> List[int]:
    '''Reads list of int numbers from stdin line'''

    int_list = [int(n) for n in input().split()]

    return int_list

def read_pair() -> List[int]:
    '''Reads pair of int numbers from stdin line'''

    pair_list = read_int_list()

    if len(pair_list) != 2:
        raise Exception('Unexpected list length')

    return pair_list

def read_data() -> Tuple[List[List[int]], List[int]]:
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

    dots_list = read_int_list()
    fact_number_of_dots = len(dots_list)
    if fact_number_of_dots != number_of_dots:
        raise Exception(
            f'Unexpected number of dots; expected: {number_of_dots}; fact: {fact_number_of_dots}')

    print('dots_list:', dots_list)

    return segments_list, dots_list

def count_dots_in_segments(segments_list, dots_list):
    '''
    Counts the number of segments that contain points

    Returns the list of intersections numbers
    '''

    return segments_list, dots_list


if __name__ == '__main__':
    input_segments_list, input_dots_list = read_data()
    list_of_intersections = count_dots_in_segments(input_segments_list, input_dots_list)
    print(' '.join(list_of_intersections))
