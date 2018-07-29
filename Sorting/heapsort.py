__about__ = """ This is a heapsort package. 
                Developed by Shreyansh. """

def heapify(arr, n, i):
	largest = i # Initialize largest as root
	left = 2 * i + 1	 # left = 2*i + 1
	right = 2 * i + 2	 # right = 2*i + 2
	# See if left child of root exists and is
	# greater than root
	if left < n and arr[i] < arr[left]:
		largest = left

	# See if right child of root exists and is
	# greater than root
	if right < n and arr[largest] < arr[right]:
		largest = right

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7, 99, 66, 1, 221, 144, 11, 21, 22, 33, 44, 20, 88, 76]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
	print ("%d" %arr[i]),
