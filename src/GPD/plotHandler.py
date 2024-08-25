import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
import random

def plot_and_save(data_x_file, h_data_file, namePlot, output_dir='outputs/plots'):
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

    plt.xlabel('X-axis Data Points')
    plt.ylabel(namePlot+ 'Values')
    plt.title('Plot of' + namePlot + 'Values vs X-axis Data Points')
    plt.legend()
    plt.grid(True)

    # Create the output file name with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_num = random.randint(1000, 9999)
    output_file = os.path.join(output_dir, f'plot_{timestamp}_{random_num}.png')
    # Save the plot as a PNG file
    plt.savefig(output_file)
    plt.close()  # Close the figure to free memory

    print(f'Plot saved as: {output_file}')
