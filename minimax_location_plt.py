import numpy as np
import matplotlib.pyplot as plt

def minimax_location(subdivisions):
    # Extract x and y coordinates from the subdivisions
    x_coords = np.array([loc[0] for loc in subdivisions])
    y_coords = np.array([loc[1] for loc in subdivisions])
    
    # Calculate c1, c2, c3, c4, c5
    c1 = np.min(x_coords + y_coords)  # Minimum of (x + y)
    c2 = np.max(x_coords + y_coords)  # Maximum of (x + y)
    c3 = np.min(-x_coords + y_coords)  # Minimum of (-x + y)
    c4 = np.max(-x_coords + y_coords)  # Maximum of (-x + y)
    c5 = max(c2 - c1, c4 - c3)  # Maximum of (c2 - c1) and (c4 - c3)

    # Calculate the optimal points
    point1 = ((c1 - c3) / 2, (c1 + c3 + c5) / 2)
    point2 = ((c2 - c4) / 2, (c2 + c4 - c5) / 2)

    return point1, point2, c5

def plot_facilities_and_optimal_locations(subdivisions, optimal_points):
    # Extract x and y coordinates from subdivisions
    x_coords = [loc[0] for loc in subdivisions]
    y_coords = [loc[1] for loc in subdivisions]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot subdivisions
    plt.scatter(x_coords, y_coords, color='blue', label='Subdivisions', marker='o')
    
    # Plot optimal locations
    plt.scatter(optimal_points[0][0], optimal_points[0][1], color='red', label='Optimal Location 1', marker='x', s=100)
    plt.scatter(optimal_points[1][0], optimal_points[1][1], color='orange', label='Optimal Location 2', marker='x', s=100)
    
    # Draw lines between subdivisions and optimal points
    for loc in subdivisions:
        plt.plot([loc[0], optimal_points[0][0]], [loc[1], optimal_points[0][1]], color='gray', linestyle='--', alpha=0.5)
        plt.plot([loc[0], optimal_points[1][0]], [loc[1], optimal_points[1][1]], color='gray', linestyle='--', alpha=0.5)

    # Set plot title and labels
    plt.title('Emergency Service Facility Location')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlim(0, 15)
    plt.ylim(0, 15)
    plt.show()

# Subdivision coordinates
subdivisions = [
    (4, 3),   # A
    (5, 11),  # B
    (13, 13), # C
    (10, 6),  # D
    (4, 6),   # E
    (10, 10), # F
    (14, 2)   # G
]

# Determine the optimal location
optimal_points = minimax_location(subdivisions)

# Output the results
print(f"Optimal Location Points: {optimal_points[0]} and {optimal_points[1]}")
print(f"Maximum Distance (c5): {optimal_points[2]}")

# Plot the facilities and optimal locations
plot_facilities_and_optimal_locations(subdivisions, optimal_points)
