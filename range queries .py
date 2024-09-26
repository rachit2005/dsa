# bowling problem 
# we have total of 7 bowl

'''score = [2,5,3,2,1,4,3]
print("index starts at 0")

l = int(input("left index: "))
r = int(input("right index: "))
sum = 0

for i in score[l:r+1]:
    # we are iterating over [l ,r] so we sum total of (r-l+1) indices eg = [2,5] we add indexes --> 2+3+4+5
    sum +=i

    
print(sum)
'''

'''Prefix Sum Array'''
# each number in the list stores the sum of all numbers before it and itself
# sum of elements [l,r] = psa[r] - psa[l-1]
# eg --> sum [2,4] == psa[4] - psa[1] --> a(1) + a(2) +a(3) + a(4) - (a(1)) == a(2) + a(3) + a(4) thats answer

def psa(arr):
    val = 0
    answer = []
    for i in range(len(arr)):
        val += arr[i]
        answer.append(val)

    return answer

arr = [1,2,3,4,5,6,7,8,9]
result = psa(arr=arr)

print(f"psa result --> {result}")

# now we have to find the sum b/w [2,4] , so we psa[4] - psa[2-1]
print(f"sum of [2,4] --> {result[4] - result[2-1]} == {3+4+5}")