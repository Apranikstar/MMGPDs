import csv

def get_flavour_values(dataFilename, flavourKeyList):
    # Initialize an empty dictionary to store the results
    result = {}



    # Open the CSV file
    with open(dataFilename, newline='') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)

        # Iterate through each row in the CSV
        for row in csvreader:
            # Extract the flavour key from the first column
            flavour = row[0]
            
            # Check if the current flavour key is in the flavourKeyList
            if flavour in flavourKeyList:
                # Convert each of the remaining elements to float and store them
                result[flavour] = [eval(value) for value in row[1:]]
    
    return result


