# Max-Heapify function
def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap it with the largest child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)  # Recursively heapify the affected subtree

# Build the max heap
def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each subtree
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# Main Heapsort function
def heapsort(arr):
    n = len(arr)
    
    # Step 1: Build a max-heap
    build_max_heap(arr)
    
    # Step 2: One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap current root with last element
        max_heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("Original array:", arr)
    heapsort(arr)
    print("Sorted array:", arr)
