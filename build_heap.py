# python3
#Elīna Miltiņa 221RDC017 18.grupa
import os

def build_heap(data, swaps, i, n):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    min_index = i
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        build_heap(data, swaps, min_index, n)

def main():
    ievade = input("I or F: ")
    if "I" in ievade.upper():
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements: ").split()))
        assert len(data) == n
    elif "F" in ievade.upper():
        fails = input("Enter the file name: ")
        atrasanas = './tests/'
        faila_vieta = os.path.join(atrasanas, fails)
        with open(faila_vieta, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        print("Invalid input. Please enter 'I' or 'F'.")
        return
    
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        build_heap(data, swaps, i, n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

