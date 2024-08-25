import csv

def save_dict_to_csv(data, filename):
    """
    Save a dictionary where keys are labels and values are lists of data to a CSV file.

    Parameters:
    - data (dict): Dictionary where keys are labels and values are lists of data.
    - filename (str): The name of the CSV file to save the data to.
    """
    # Check if the dictionary is empty
    if not data:
        raise ValueError("The dictionary is empty")

    # Get the maximum length of the lists in the dictionary
    max_length = max(len(v) for v in data.values())

    # Write to CSV file
    with open("outputs/rawData/"+filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        header = ["Index"] + list(data.keys())
        writer.writerow(header)
        
        # Write the rows
        for i in range(max_length):
            row = [i + 1]  # Index starting from 1
            for flavour in data:
                # Append the value if available, otherwise leave it blank
                row.append(data[flavour][i] if i < len(data[flavour]) else "")
            writer.writerow(row)

    print(f"Data successfully saved to {filename}")




def write_list_to_csv(data, filename):
    """
    Write a list of elements to a CSV file, each element in its own row (single column).

    Args:
        filename (str): The name of the CSV file to write.
        data (list): The data to write to the CSV file, where each element represents a row.
    """
    try:
        # Ensure each element is wrapped in a list
        data = [[element] for element in data]

        with open("outputs/rawData/" + filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

