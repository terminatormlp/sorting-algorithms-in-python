import matplotlib.pyplot as plt
import numpy as np
import time
from numpy import random


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Keep track of whether any swaps are made during this iteration
        swapped = False
        
        # Iterate through the unsorted part of the array
        for j in range(n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swaps were made during this iteration, the array is sorted
        if not swapped:
            break
        
        # Plot the current state of the array
        plt.bar(np.arange(len(arr)), arr, color='b')
        plt.title("Bubble Sort")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.draw()
        plt.pause(0.1)  # Add a delay of 0.1 seconds
        plt.clf()  # Clear the plot
    
    return arr


# Test the function
arr = random.rand(5)
sorted_arr = bubble_sort(arr)
print(sorted_arr)
