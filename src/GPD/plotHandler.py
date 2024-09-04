import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
import random

def plot_and_save(data_x_file, h_data_file, namePlot, output_dir='outputs/plots', log_y=False):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the data
    data_points_x = pd.read_csv(data_x_file, header=None).values.flatten()
    h_data = pd.read_csv(h_data_file)

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Iterate over the columns in the H.csv file (excluding 'Index')
    for column in h_data.columns:
        if column != 'Index':
            plt.plot(data_points_x, h_data[column], label=column)

    # Set the x-axis to a logarithmic scale and set the limits
    plt.xscale('log')
    plt.xlim(0.001, 1)

    if log_y:
        plt.yscale('log')  # Set the y-axis to a logarithmic scale, not recommended if data includes negative values

    # Automatically adjust y-axis based on the min and max values in the data
    min_y_value = h_data.drop(columns=['Index'], errors='ignore').values.min()
    max_y_value = h_data.drop(columns=['Index'], errors='ignore').values.max()
    y_padding = (max_y_value - min_y_value) * 0.1  # Add 10% padding
    plt.ylim(min_y_value - y_padding, max_y_value + y_padding)  # Set y-axis limits with padding

    plt.xlabel('X-axis Data Points')
    plt.ylabel(namePlot + ' Values')
    plt.title('Plot of ' + namePlot + ' Values vs X-axis Data Points')
    
    # Move the legend below the plot
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)  # Adjust ncol for number of columns

    plt.grid(True)

    # Create the output file name with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_num = random.randint(1000, 9999)
    output_file = os.path.join(output_dir, f'plot_{timestamp}_{random_num}.png')
    # Save the plot as a PNG file
    plt.savefig(output_file, bbox_inches='tight')  # Use bbox_inches to include the legend
    plt.close()  # Close the figure to free memory

    print(f'Plot saved as: {output_file}')
