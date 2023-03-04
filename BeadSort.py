import matplotlib.pyplot as plt

def bead_sort(arr):
    # Find the maximum number in the array
    max_num = max(arr)
    
    # Create a 2D array of beads
    beads = [[0 for _ in range(len(arr))] for _ in range(max_num)]
    for i, num in enumerate(arr):
        for j in range(num):
            beads[max_num-j-1][i] = 1
    
    # Calculate the sums of the beads in each column
    sums = [sum(col) for col in beads]
    
    # Create a color map for the plot
    cmap = plt.get_cmap('viridis')
    
    # Iterate through the columns of the 2D array
    for i in range(len(beads[0])):
        # Create a color array for the plot
        colors = [cmap(j/len(beads)) for j in range(sums[i])]
        
        # Plot the current state of the array
        plt.bar(range(len(beads)), [sum(beads[j][0:i+1]) for j in range(max_num)], color=colors)
        plt.title("Bead Sort")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.draw()
        plt.pause(0.1)
        plt.clf()
        
    # Extract the sorted array from the 2D array of beads
    sorted_arr = [sum(beads[j][0:i+1]) for j in range(max_num) for i in range(len(beads[0])) if beads[j][i] == 1]
    
    return sorted_arr

# Test the function
arr = [89, 79, 88, 75, 24, 2, 69, 27, 33, 0, 48, 8, 39, 32, 77, 16, 20, 45, 52, 68, 63, 4, 74, 1, 51, 41, 56, 80, 26, 21, 44, 19, 66, 13, 49, 47, 71, 81, 61, 70, 15, 14, 6, 25, 28, 42]
sorted_arr = bead_sort(arr)
print(sorted_arr)
