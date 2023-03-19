# python3
#Elīna Miltiņa 221RDC017 18.grupa
import os
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2,-1,-1):
        shift(data, i, swaps)
    return swaps    

def shift(data, i, swaps):
    n = len(data)
    min_index = i 
    left_c = 2 * i + 1 
    right_c = 2 * i + 2 
    if left_c < n and data[left_c] < data[min_index]: 
        min_index = left_c  
    if right_c < n and data[right_c] < data[min_index]: 
        min_index = right_c 
    if min_index != i: 
        swaps.append((i, min_index)) 
        data[i], data[min_index] = data[min_index], data[i] 
        shift(data, min_index, swaps) 
         
def main(): 
    ievade = input("I or F") 
    if "I" in ievade: 
        m = int(input()) 
        data = list(map(int, input().split())) 
        assert len(data) == m 
    elif "F" in ievade: 
        fails = input() 
        atrasanas = './tests/' 
        faila_vieta = os.path.join(atrasanas, fails) 
        with open(faila_vieta, mode="r") as file: 
            m = int(file.readline()) 
            data = list(map(int, file.readline().split())) 
    swaps = build_heap(data) 
    print(len(swaps)) 
    for i, j in swaps: 
        print(i, j) 
        
        
if __name__ == "_main_":
    main()