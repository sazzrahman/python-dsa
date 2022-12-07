
# Implement a linear search algorithm
# O(N) time complexity

import argparse


def linear_search(arr: list, n: float) -> int:
    """
    arr: a list of numbers
    n : the number to be searched
    output : the index of the found item
    """
    i = 0
    while i < len(arr):
        if arr[i] == n:
            return i
        i += 1
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arr", nargs="+", type=float)
    parser.add_argument("--n", type=float)
    args = parser.parse_args()
    print(linear_search(args.arr, args.n))
