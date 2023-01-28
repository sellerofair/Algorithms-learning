'''Reads data from stdin line'''

from typing import List


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
