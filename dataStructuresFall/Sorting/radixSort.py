def countingSort(a, exp):
    output = [0]*len(a)
    count = [0]*10

    for i in range(len(a)):
        count[a[i]//exp%10] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    i = len(a) - 1
    while i >= 0:
        output[count[a[i]//exp%10] - 1] = a[i]
        count[a[i]//exp%10] -= 1
        i -= 1

    # Difference bw couting sort and radix sort
    # for i in range(len(a)):
    #     output[count[a[i]//exp%10] - 1] = a[i]
    #     count[a[i]//exp%10] -= 1

    for i in range(len(a)):
        a[i] = output[i]

def radixSort(a):
    if not a or len(a) == 1:
        return

    maximum = max(a)
    exp = 1

    while maximum//exp > 0:
        countingSort(a, exp)
        exp *= 10

  
# Driver code to test above 
arr = [170, 45, 75, 90, 802, 24, 2, 66] 
radixSort(arr) 

print(arr)