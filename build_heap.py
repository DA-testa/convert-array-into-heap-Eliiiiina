# python3
#Elīna Miltiņa 221RDC017 18.grupa
#import os
def build_heap(data):
    swaps = []
    n = len(data)
    #for i in range(n//2,-1,-1):
     #   shift(data, i, swaps)
    #return swaps    

    # Starting from the middle, heapify each parent node
    # down to the bottom of the heap
    for i in range(n // 2 - 1, -1, -1):
        swaps += heapify(data, n, i)

    # After the heap is built, perform the actual heap sort
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        swaps.append((0, i))
        swaps += heapify(data, i, 0)

    return swaps

def heapify(data, n, i):
    swaps = []
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than parent
    if left < n and data[left] > data[largest]:
        largest = left

    # Check if right child is larger than parent
    if right < n and data[right] > data[largest]:
        largest = right

    # If one of the children is larger, swap with parent
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        swaps.append((i, largest))
        swaps += heapify(data, n, largest)

    return swaps

def main():
    # Get input from the user
    input_type = input()
    if input_type.upper() == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type.upper() == "F":
        filename = input()
        with open(filename) as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    
        return

    # Check if length of data is the same as the specified length
    if len(data) != n:
        print()
        return

    # Call build_heap to sort the data and get the swaps
    swaps = build_heap(data)

    # Output the number of swaps and the list of swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
