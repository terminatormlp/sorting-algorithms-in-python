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

        
def bogo_sort(arr):
    # Shuffle the array
    random.shuffle(arr)
    
    # Plot the shuffled array
    plt.bar(np.arange(len(arr)), arr)
    plt.title("Bogo Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.draw()
    plt.pause(0.1)
    
    # Check if the array is sorted
    while not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        # Shuffle the array
        random.shuffle(arr)
        
        # Plot the shuffled array
        plt.bar(np.arange(len(arr)), arr)
        plt.title("Bogo Sort")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.draw()
        plt.pause(0.1)
        
        # Play the sound effect
        play_sound()
        
    return arr

# Test the function
arr = np.array([3, 2, 1, 5, 4])
sorted_arr = bogo_sort(arr)
print(sorted_arr)
