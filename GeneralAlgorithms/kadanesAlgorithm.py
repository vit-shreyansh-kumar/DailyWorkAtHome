__about__ = """In computer science, the maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array,is maximal."""
# Implementation: Check for local and the global maxima. choose the max element by using max(current_element , sum_of_curr_and_previous_sum)


array = [-2, -3, 4, -1, -2, 1, 5, -3]

local_maxima = array[0]
global_maxima= array[0]

for x in array:
    local_maxima = max(x , local_maxima + x)
    
    if local_maxima > global_maxima :
        global_maxima = local_maxima
        
print("Max sub Array is:",global_maxima)
