def third_smallest(arr):

    if (len(arr) < 3):
        return "Invalid"

    first = 9999
    second = 9999
    third = 9999

    for i,v in enumerate(arr):

        if arr[i] < first :

            third = second
            second = first
            first = arr[i]

        elif arr[i] < second:

            third = second
            second = arr[i]

        elif arr[i] < third:
            third = arr[i]

    return third

y =third_smallest([1,2,3,4,5,6,7,8,9])
print(y)