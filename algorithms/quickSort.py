import argparse

# quick sort using recursion 
# uses a pivot to rearrange all the elements in the array to either left or right of the pivot
# works on each side of the pivot recursively
# average time complexity O(nlogn)
# worst case O(n2) for an already sorted array

def quick_sort(arr:list) -> list:
    """
    arr : a list of unsorted numbers
    returns a sorted list
    """
    if len(arr) <= 1:
        return arr
    i = 0
    change = 0 # the new index the pivot will be placed
    pivot = arr.pop(0)
    pivoted = arr.copy()
    
    l = len(arr)

    while i < l:
        if arr[i] <= pivot:
            change+=1
            to_move = pivoted.pop(i)
            pivoted.insert(change-1,to_move)
            i+=1
        else:
            i+=1
    pivoted.insert(change,pivot)

    # call quick sort on the left side and right side
    return quick_sort(pivoted[0:change]) + [pivot] + quick_sort(pivoted[change+1:])
    
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arr",nargs="+",type=float)
    args = parser.parse_args()
    print(quick_sort(args.arr))


