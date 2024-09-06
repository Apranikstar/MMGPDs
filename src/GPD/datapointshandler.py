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
    print("\n" + "#" * 40)
    print("           KINEMATIC DATA POINTS          ")
    print("#" * 40 + "\n")
    print("Choose your scenario for calculations:")
    print("1. Single Kinematic Point Calculation")
    print("2. Multiple Kinematic Points Calculation\n")
    scenario = input("Please enter the scenario number (1 or 2): ")

    if scenario == "1":
        results = []
        print("\nYou selected: Single Kinematic Point Calculation")
        print("Please provide the values for x, Q², and t.")
        ah.AnalysisDefualtDataPoints("Single")

        kinematicPoint = input("\nEnter the values in the following order separated by commas (x, Q², t): \n")
        Values = [value.strip() for value in kinematicPoint.split(",")]
        for items in Values:
            results.append(items)
        print("\nThe kinematic point provided is:", results)
        print("\n" + "#" * 40)
        print("  KINEMATIC POINT RETRIEVED SUCCESSFULLY  ")
        print("#" * 40 + "\n")
        return results
    
    elif scenario == "2":
        print("\nYou selected: Multiple Kinematic Points Calculation")
        print("In this scenario, two of the three variables will be constant, and one will vary over an interval.")
        print("Please enter the kinematic variables using the following format:\n")
        print("Examples:")
        print("[x] | [Q²] | [t1, t2, points]")
        print("[x] | [Q²(1), Q²(2), points] | [t]")
        print("[x1, x2, points] | Q² | t\n")
        ah.AnalysisDefualtDataPoints("Multiple")
        Values = input("Enter the corresponding values with the notation explained above:\n")
        parsedValues = split_by_delimiter(Values)  ## A list of [x,Q2,t]
        ###print("Parsed values are: ", parsedValues)
        outputDatapoints = ListToFuncArgs(parsedValues)
        ###print("\nOutput data points:", outputDatapoints)
        print("\n" + "#" * 40)
        print("  DATA POINTS RETRIEVED SUCCESSFULLY  ")
        print("#" * 40 + "\n")
        return outputDatapoints
    else:
        print("\nInvalid input. Please enter 1 or 2.")


