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

        
def bubble_sort(arr):
    # Plot the initial array
    plt.bar(np.arange(len(arr)), arr)
    plt.title("Bubble Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.draw()
    plt.pause(0.1)
    
    # Sort the array using bubble sort
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            # Compare adjacent elements and swap them if they're in the wrong order
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Plot the updated array
                plt.bar(np.arange(len(arr)), arr)
                plt.title("Bubble Sort")
                plt.xlabel("Index")
                plt.ylabel("Value")
                plt.draw()
                plt.pause(0.1)
                
                # Play the sound effect
                play_sound()
    
    return arr

# Generate a random array
arr = np.random.randint(1, 100, 10)

# Test the function
sorted_arr = bubble_sort(arr)
print(sorted_arr)
