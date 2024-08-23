import numpy as np
import re
import ast
import src.GPD.analysishandler as ah




def generate_skewed_random_values(initial, final, num_points):
    """
    Generate random values between `initial` and `final` with a bias towards `initial`.

    Parameters:
    - initial (float): The lower bound of the range.
    - final (float): The upper bound of the range.
    - num_points (int): The number of random values to generate.

    Returns:
    - np.ndarray: Array of generated random values.
    """
    # Ensure initial is less than final
    if initial >= final:
        raise ValueError("Initial value must be less than final value")

    # Generate values in the range [0, 1]
    uniform_random_values = np.random.rand(num_points)
    
    # Apply the transformation to skew values towards initial
    skewed_values = np.power(uniform_random_values,3)
    
    # Transform values back to the range [initial, final], If you're confused the second part is calculated first.
    scaled_values = initial + (final - initial) * skewed_values
    # Remove zero values
    non_zero_values = scaled_values[scaled_values != initial]

    # Sort the values in ascending order
    sorted_values = np.sort(non_zero_values)
    return sorted_values


##########################################################################

def split_by_delimiter(input_string, delimiter='|'):
    # Split the string by the delimiter
    parts = input_string.split(delimiter)
    parts = [re.sub(r'\s+', '', s) for s in parts]
    # Return the list of parts
    return parts


##########################################################################
def ListToFuncArgs(parsedValues):
    result = []
    parsedValues = [ast.literal_eval(item) for item in parsedValues]
    for items in parsedValues:
        print("Processing items:", items)  # Debugging line
        if len(items) == 1:
            try:
                result.append(float(items[0]))
            except ValueError as e:
                print(f"Error converting {items[0]} to int: {e}")
        elif len(items) == 3:
            try:
                start = int(items[0])
                stop = int(items[1])
                points = int(items[2])
                result.append(generate_skewed_random_values(start, stop, points))
            except ValueError as e:
                print(f"Error converting {items} to linspace: {e}")
        else:
            raise ValueError(f"Unexpected number of elements in items: {len(items)}")
    
    return result




def GetDataPoints():
    print("##############DATAPOINTS##################")
    print("We have two scenarios of calculations.\n1. Single kinematic point Calculations.")
    print("2. Multiple kinematic points")
    scenario = input("Which scenario do you want to pick? Write down the scenario number: ")

    if scenario == "1":
        results = []
        print("We need you to provide the values for x, Q2, t")
        ah.AnalysisDefualtDataPoints("Single")

        kinematicPoint = input("Write down the variables in the same sequence as explained with commas (,) seperating them: \n")
        Values = [value.strip() for value in kinematicPoint.split(",")]
        for items in Values:
            results.append(items)
        print("The kinematic point is: ", results)
        print("##############DATAPOINTS RETRIEVED SUCCESFULLY!##################")
        return results
    
    elif scenario == "2":
        print("In this scenario we need two of the three variables as constants, and one will be treated as an interval. ")
        print("Now you have to enter the kinematic variables inside brackets and use a delimiter to seperate variables.")
        print("examples: \n [x]|[Q2]| [t1,t2, points]  ")
        print(" [x] | [Q2(1) , Q2(2), points]   | [t]")
        print(" [x1,x2, points] | Q2 | t ")
        ah.AnalysisDefualtDataPoints("Multiple")
        Values = input("Enter the corrosponding values with the notation explained before: \n")
        parsedValues = split_by_delimiter(Values)  ## A list of [x,Q2,t]
        print("Parsed values are: ", parsedValues)
        outputDatapoints = ListToFuncArgs(parsedValues)
        print("Output data are: ", outputDatapoints)
        print("##############DATAPOINTS RETRIEVED SUCCESFULLY!##################")
        return outputDatapoints
    else:
        print("Wrong input!")


