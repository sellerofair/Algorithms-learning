'''
Inversions number

Merge sorting practice
'''

from typing import List, Tuple


def merge_sort(numbers_list: List[int], start: int, end: int) -> Tuple[List[int], int]:
    '''
    Returns tuple of:
        - sorted part of list from start to end;
        - number of inversions (measure of disorder).

    numbers_list - source list of integer numbers;
    start - included start index in numbers_list;
    end - not included end index in numbers_list;
    '''

    numbers_count = end - start
    if numbers_count == 0:
        return [], 0

    if numbers_count == 1:
        return [numbers_list[start]], 0

    i_middle = numbers_count // 2
    middle = start + i_middle

    left_sorted_part, left_inversions_number = merge_sort(numbers_list, start, middle)
    right_sorted_part, right_inversions_number = merge_sort(numbers_list, middle, end)

    total_inversions_number = left_inversions_number + right_inversions_number

    i_left = 0
    i_right = 0
    for i in range(start, end):
        if i_left == middle - start:
            numbers_list[i] = right_sorted_part[i_right]
            i_right += 1
            total_inversions_number += i_middle - i_left

        elif i_right == end - middle:
            numbers_list[i] = left_sorted_part[i_left]
            i_left += 1

        elif left_sorted_part[i_left] > right_sorted_part[i_right]:
            numbers_list[i] = right_sorted_part[i_right]
            i_right += 1
            total_inversions_number += i_middle - i_left

        else:
            numbers_list[i] = left_sorted_part[i_left]
            i_left += 1

    return numbers_list[start:end], total_inversions_number

def sort() -> Tuple[List[int], int]:
    '''
    Waiting for stdin by lines:
        - count of numbers in list;
        - list of numbers separated by a space

    Returns tuple of:
        - sorted list;
        - number of inversions (measure of disorder).
    '''

    numbers_count = int(input())
    numbers_list = [int(n) for n in input().split()]

    result = merge_sort(numbers_list, 0, numbers_count)

    print('sorted_list:', result[0])
    print('inversions_number:', result[1])

    return result


if __name__ == '__main__':
    sort()
