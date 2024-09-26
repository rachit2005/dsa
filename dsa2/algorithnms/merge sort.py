def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_list(left , right , arr)


def merge_two_list(a,b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k =0

    while i  < len_a and j < len_b:
        if a[i] <=b[j]:
            arr[k] = a[i]
            i+=1
            
        elif a[i] > b[j]:
            arr[k] = b[j]
            j+=1

        k +=1

    while i < len_a:
        arr[k] = a[i]
        i +=1
        k+=1
        
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

    

if __name__ == "__main__":
    arr = [10,3,15,67,9,11,45354,43,54,23,56566565,7,88,19]
    merge_sort(arr)
    print(arr)