import matplotlib.pyplot as plt
import numpy as np
import time
from numpy import random


def radix_sort(arr):
    # Convert the floating-point numbers to integers
    arr = np.round(arr * 1000).astype(int)
    
    # Find the maximum number in the array
    max_num = max(arr)
    
    # Find the number of digits in the maximum number
    num_digits = len(str(max_num))
    
    # Define a color map for the plot
    cmap = plt.get_cmap('tab20c')
    
    # Set the background color of the plot
    plt.style.use('dark_background')
    
    # Create a legend for the plot
    legend_labels = [f"Digit {i+1}" for i in range(num_digits)]
    plt.legend(legend_labels, loc='upper left')
    
    # Iterate through each digit
    for digit in range(num_digits):
        # Create 10 buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]
        
        # Place each number in the appropriate bucket based on its digit
        for num in arr:
            digit_value = (num // 10**digit) % 10
            buckets[digit_value].append(num)
        
        # Concatenate all the buckets to get the new array
        arr = np.array([num for bucket in buckets for num in bucket])
        
        # Create a color array for the plot
        colors = [cmap(i/len(arr)) for i in range(len(arr))]
        
        # Plot the current state of the array
        plt.bar(np.arange(len(arr)), arr, color=colors)
        plt.title(f"Radix Sort (Sorting by Digit {digit+1})")
        plt.xlabel("Index")
        plt.ylabel("Value")
        
        # Add text to show the current digit being sorted
        plt.text(len(arr)*0.95, max_num*0.95, f"Sorting by Digit {digit+1}", fontsize=12, color='white', ha='right', va='top')
        
        plt.draw()
        plt.pause(1.5)  # Add a delay of 1.5 seconds
        plt.clf()  # Clear the plot
        
    # Convert the integers back to floating-point numbers
    arr = arr / 1000
    
    return arr

# Test the function
arr = random.rand(1532)
sorted_arr = radix_sort(arr)
print(sorted_arr)
