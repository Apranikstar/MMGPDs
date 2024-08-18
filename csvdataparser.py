from uncertainties import ufloat
import csv


def parse_value(value_str):
    """Parse a value of the form 'value+0' and return a ufloat."""
    # Split the string at the '+' symbol to separate the value and the uncertainty
    value, uncertainty = value_str.split('+')
    # Convert the value to a float, uncertainty is 0 in this case
    value = float(value)
    uncertainty = float(uncertainty)  # This is always 0 in your case
    # Return the ufloat
    return ufloat(value, uncertainty)

def process_csv(file_path, keys=None):
    """Process the CSV file and return ufloats for the specified keys."""
    data = {}
    
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # The first element is the key (e.g., "uv", "dv", etc.)
            key = row[0].strip('"')
            
            if keys is None or key in keys:
                # The rest of the row contains the values
                values = [parse_value(v) for v in row[1:]]
                data[key] = values
                
    return data