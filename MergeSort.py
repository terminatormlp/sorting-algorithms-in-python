import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import random
import platform

# Define the sound effect function for Windows
if platform.system() == 'Windows':
    import winsound
    
    def play_sound():
        frequency = 2000  # Set the frequency (Hz)
        duration = 200  # Set the duration (ms)
        winsound.Beep(frequency, duration)
        
# Define the sound effect function for Linux and macOS
else:
    import os
    import subprocess
    
    def play_sound():
        subprocess.call(['afplay', '/System/Library/Sounds/Ping.aiff'])


def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    sorted_arr = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] <= right_half[right_idx]:
            sorted_arr.append(left_half[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right_half[right_idx])
            right_idx += 1
    
    # Append the remaining elements
    sorted_arr.extend(left_half[left_idx:])
    sorted_arr.extend(right_half[right_idx:])
    
    # Plot the sorted array
    plt.bar(np.arange(len(sorted_arr)), sorted_arr)
    plt.title("Merge Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.draw()
    plt.pause(0.1)
    
    # Play the sound effect
    play_sound()
    
    return sorted_arr


# Generate a random array
arr = np.random.randint(1, 100, 100)

# Test the function
sorted_arr = merge_sort(arr)
print(sorted_arr)
