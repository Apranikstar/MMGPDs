"""
This file contains two functions. 
The GetAnalysisParameters() reads the components of /data directory 
in the /data directory all of the MMGPA analysises are available.
Each analysis contains multiple GPD sets evaluated.


"""
import os 
import csv

def AnalysisComputationInstructions(analysisName):
    if analysisName == "HGAG23":
        return ["H", "E", "Ht"]
    else: 
        print("No available GPDs found!")

#######################################################################################


def AnalysisDefualtDataPoints(SingleOrMultiple):
    if SingleOrMultiple == "Single":
        print ("HGAG23 default variables  x,Q2,t:    0.25,4,-1         ")
    elif SingleOrMultiple == "Multiple":
        print ("HGAG23 default variables [x]|[Q2]|[t] : [0,1,100]|[4]|[-1]")






############################################################################################
def GetAnalysisParameters():
    #Listing All analysises
    analysisList = [d for d in os.listdir("data") if os.path.isdir(os.path.join("data", d))]
    print("################################")
    print(analysisList)
    #User choses an analysis
    userAnalysisInput = input("Which analysis do you want to use to perform the calculations? \n")
    userAnalysisInput = userAnalysisInput.strip()
    #Time to pick a parameter set
    csv_files=[]
    for file_name in os.listdir("data/"+userAnalysisInput):
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            csv_files.append(file_name.rsplit('.', 1)[0])
    # Prints the list of CSV file names
    print("################################")
    #print("Parameter sets:", sorted(csv_files,key = int)) ## THIS MAY RESULTS IN A BUGGY CODE
    print("GPDs set:",csv_files)
    userGPDSetInput = input("which of these GPDs set do you want to use? \n")
    userGPDSetInput = userGPDSetInput.strip()
    
    #######################
    print("################################")
    print(AnalysisComputationInstructions(userAnalysisInput))
    print("Which GPDs do you want to calculate?")
    userGPDList = input("Use commas to seperate. Write A for all: \n")
    if userGPDList == "A":
       userGPDList = AnalysisComputationInstructions(userAnalysisInput)
    else:
       userGPDList = [item.strip() for item in userGPDList.split(",")]

    print("################################")
    flavourList = []
    #csvFileName = "data/" + userAnalysisInput+ "/" +userPrameterSet+ ".csv"
    with open("data/" + userAnalysisInput+ "/" +userGPDSetInput+ ".csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Append the first element of each row to the list
            if row:  # Ensure the row is not empty
                flavourList.append(row[0])
    print(flavourList)
    userFlavourInputs = input("Which one of these flavour do you want to use? You can write A for all of them. ")
    if userFlavourInputs == "A":
        print("You Analysis summary is: \n",[userAnalysisInput, userGPDSetInput,userGPDList, flavourList ])
        print("################################")
        return [userAnalysisInput, userGPDSetInput,userGPDList, flavourList ]
    else:
        if ',' in userFlavourInputs:
            userFlavourInputs = userFlavourInputs.split(',')
            userFlavourInputs = [s.strip() for s in userFlavourInputs]
            print("You Analysis summary is: \n",[userAnalysisInput,userGPDSetInput,userGPDList, userFlavourInputs])
            print("################################")
            return [userAnalysisInput,userGPDSetInput,userGPDList, userFlavourInputs]
        else:
            userFlavourInputs = [userFlavourInputs.strip()]
            print("You Analysis summary is: \n",[userAnalysisInput,userGPDSetInput, userGPDList, userFlavourInputs])
            print("################################")
            return [userAnalysisInput,userGPDSetInput, userGPDList, userFlavourInputs]




