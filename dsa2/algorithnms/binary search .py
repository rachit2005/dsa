from time_efficiency import time_it

@time_it
def linear_search(n_list , find):
    for index , element in enumerate(n_list):
        if element == find:
            return index
    return -1

@time_it
def binary_search(n_list , find):
    n_list.sort()
    l = 0
    h = len(n_list) - 1
    
    while l <= h:
        mid = (h+l)//2

        if find == n_list[mid]:
            return mid

        elif find > n_list[mid]:
            l = mid+1

        else:
            h = mid - 1

    return -1

# now we are using recursion for binary searches 
def binary_search_recursion(n_list , find , l , h):
    n_list.sort()
    if l>h:
        return -1
    
    mid = (l+h)//2
    if mid >= len(n_list) or mid<0:
        return -1
    
    if find == n_list[mid]:
        return mid

    elif find>n_list[mid]:
        l = mid+1
    else:
        h = mid-1

    return binary_search_recursion(n_list , find , l , h)


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find) # finding the index of 1st occurence
    indices = [index] # creating the list of indices with the 1st occurence

    # find indices on left hand side

    i = index-1 # starting from the prev index of the 1st occurence and continuously decreasing to check the left side of the list
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i -= 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i += 1

    return sorted(indices)


    


if __name__ == "__main__":
    list1 = [12,3,4,3,54,67,6,869,67,234,4564]
    # find = 1

    # list1 = [i for i in range(100000)]
    find = 869

    # print(f'finding {find} --> {linear_search(list1 , find)}')
    # print(binary_search(list1 , find))
    # print(binary_search_recursion(list1 , find , 0 , len(list1)- 1))

    print(find_all_occurances(list1 , 3))
