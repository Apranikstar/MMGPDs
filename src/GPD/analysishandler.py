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
    analysisList = [d for d in os.listdir("src/GPD/data") if os.path.isdir(os.path.join("src/GPD/data", d))]
    print("################################")
    print(analysisList)
    #User choses an analysis
    userAnalysisInput = input("Which analysis do you want to use to perform the calculations? \n")
    userAnalysisInput = userAnalysisInput.strip() 
    #Time to pick a parameter set
    csv_files=[]
    for file_name in os.listdir("src/GPD/data/"+userAnalysisInput+"/H"):
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
    ################################


    flavourListH = []
    #csvFileName = "src/GPD/data/" + userAnalysisInput+ "/" +userPrameterSet+ ".csv"
    with open("src/GPD/data/" + userAnalysisInput+ "/H/" +userGPDSetInput+ ".csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Append the first element of each row to the list
            if row:  # Ensure the row is not empty
                flavourListH.append(row[0])


    flavourListHt = []
    #csvFileName = "src/GPD/data/" + userAnalysisInput+ "/" +userPrameterSet+ ".csv"
    with open("src/GPD/data/" + userAnalysisInput+ "/Ht/" +userGPDSetInput+ ".csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Append the first element of each row to the list
            if row:  # Ensure the row is not empty
                flavourListHt.append(row[0])


    flavourListE = []
    #csvFileName = "src/GPD/data/" + userAnalysisInput+ "/" +userPrameterSet+ ".csv"
    with open("src/GPD/data/" + userAnalysisInput+ "/E/" +userGPDSetInput+ ".csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Append the first element of each row to the list
            if row:  # Ensure the row is not empty
                flavourListE.append(row[0])


    analysisHandlerOutput = []
    #print("H flavour list: ", flavourListH)
    #print("Ht flavour list: ",flavourListHt)
    #print("E flavour list: ",flavourListE)
    userHFlavourInputs = None
    userHtFlavourInputs = None
    userEFlavourInputs = None
    if "H" in userGPDList:
        print("H flavour list: ", flavourListH)
        userHFlavourInputs = input("Which one of these flavour do you want to use? You can write A for all of them. ")
        if userHFlavourInputs == "A":
            userHFlavourInputs = flavourListH
        else:
            if ',' in userHFlavourInputs:
                userHFlavourInputs = userFlavourInputs.split(',')
                userHFlavourInputs = [s.strip() for s in userHFlavourInputs]

    if "Ht" in userGPDList:
        print("Ht flavour list: ", flavourListHt)
        userHtFlavourInputs = input("Which one of these flavour do you want to use? You can write A for all of them. ")
        if userHtFlavourInputs == "A":
            userHtFlavourInputs = flavourListHt
        else:
            if ',' in userHtFlavourInputs:
                userHtFlavourInputs = userFlavourInputs.split(',')
                userHtFlavourInputs = [s.strip() for s in userHtFlavourInputs]

    if "E" in userGPDList:
        print("E flavour list: ", flavourListE)
        userEFlavourInputs = input("Which one of these flavour do you want to use? You can write A for all of them. ")
        if userEFlavourInputs == "A":
            userEFlavourInputs = flavourListE
        else:
            if ',' in userEFlavourInputs:
                userEFlavourInputs = userFlavourInputs.split(',')
                userEFlavourInputs = [s.strip() for s in userEFlavourInputs]

    analysisHandlerOutput= [userAnalysisInput, userGPDSetInput, userGPDList, userHFlavourInputs, userHtFlavourInputs, userEFlavourInputs ]
    return analysisHandlerOutput





