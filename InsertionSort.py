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

        
def insertion_sort(arr):
    # Plot the initial array
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(arr)), arr, color='b')
    ax.set_title("Insertion Sort")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    plt.draw()
    plt.pause(0.1)
    
    # Sort the array using insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
        # Plot the updated array
        ax.clear()
        ax.bar(np.arange(len(arr)), arr, color='b')
        ax.set_title("Insertion Sort")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        plt.draw()
        plt.pause(0.1)
                
        # Play the sound effect
        play_sound()
    
    return arr

# Generate a random array
arr = np.random.randint(1, 100, 50)

# Test the function
sorted_arr = insertion_sort(arr)
print(sorted_arr)
