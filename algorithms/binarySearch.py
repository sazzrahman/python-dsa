import argparse


# the input array must be sorted
# the recursive call ensures O(logN) time

def binary_search(arr: list, n: float) -> int:
    """
    arr: a list of sorted numbers
    n : the number to be searched
    i : starting index
    output : the index of the found item
    """
    l = len(arr)
    h = l//2
    if n >= arr[h]:
        if n == arr[h]:
            return h
        else:
            binary_search(arr[h+1:], n)
    else:
        return binary_search(arr[0:h], n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arr", nargs="+", type=float)
    parser.add_argument("--n", type=float)
    args = parser.parse_args()
    print(binary_search(args.arr, args.n))
