def shell_sort(elements):
    size = len(elements)
    gap = size//2

    while gap>0:
        for i in range(gap , size):
            anchor = elements[i]
            j = i
            while j>=gap and elements[j-gap] > anchor:
                elements[j] = elements[j-gap]       
                j -= gap

            elements[j] = anchor

        gap = gap//2

def find_min(arr):
    min = 100000000000000000000000000000000000000000000000000000
    for i in range(len(arr)):
        if arr[i]<min:
            min = arr[i]
    return min

def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(min_index+1 , size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i] , arr[min_index] = arr[min_index] , arr[i]
        

if __name__ == "__main__":
    elements = [0,21,38,29,17,4,6,546,56,34,1,5]
    # shell_sort(elements)
    selection_sort(elements)
    print(elements)