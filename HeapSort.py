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


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # Check if left child of root exists and is greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # Check if right child of root exists and is greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap

            # Plot the updated array
            plt.bar(np.arange(len(arr)), arr)
            plt.title("Heap Sort")
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.draw()
            plt.pause(0.1)

            # Play the sound effect
            play_sound()

            # Heapify the root
            heapify(arr, n, largest)

    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap

        # Plot the updated array
        plt.bar(np.arange(len(arr)), arr)
        plt.title("Heap Sort")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.draw()
        plt.pause(0.1)

        # Play the sound effect
        play_sound()

        # Heapify root element
        heapify(arr, i, 0)

    # Plot the sorted array
    plt.bar(np.arange(len(arr)), arr)
    plt.title("Heap Sort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.draw()
    plt.pause(0.1)

    # Play the sound effect
    play_sound()

    return arr


# Generate a random array
arr = np.random.randint(1, 1000, 10)

# Test the function
sorted_arr = heap_sort(arr)
print(sorted_arr)
