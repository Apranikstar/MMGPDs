import numpy as np
import src.GPD.csvdataparser as csvdataparser

def computationHandeler(parameters, x):
    results =[]
    for points in x:
        funcAtPoint = parameters[0] * np.power(1 - points, 3) * np.log(1/points) + parameters[1] * np.power(1 - points, 3) + parameters[2] * points * np.power(1-points,2)
        results.append(funcAtPoint)
    return results


def _profileFuncH(analysisVariables, x): #["Analysis", "GPDs set", "GPD to calc", [Flavour List] , X ]
    print("Calculating profile functions: ")
    if isinstance(x, np.ndarray):
        x = x.tolist()
        print("X: ",x)
    else:
        x = [float(x)]
        print("X:", x)

    



    dataFile = "src/GPD/data/"+analysisVariables[0]+"/H/"+analysisVariables[1]+".csv"
    flavourKeyList = analysisVariables[3]
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) # returns a dict: dict["flavours"] = [aprime,B,A]

    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)

    print("results:",results )
    print("################################")
    return results


def _profileFuncHt(analysisVariables, x): #["Analysis", "GPDs set", "GPD to calc", [Flavour List] , X ]
    print("Calculating profile functions: ")
    if isinstance(x, np.ndarray):
        x = x.tolist()
        print("X: ",x)
    else:
        x = [float(x)]
        print("X:", x)



    dataFile = "src/GPD/data/"+analysisVariables[0]+"/Ht/"+analysisVariables[1]+".csv"
    flavourKeyList = analysisVariables[4]
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) # returns a dict: dict["flavours"] = [aprime,B,A]

    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)

    print("results:",results )
    print("################################")
    return results
    

def _profileFuncE(analysisVariables, x): #["Analysis", "GPDs set", "GPD to calc", [Flavour List] , X ]
    print("Calculating profile functions: ")
    if isinstance(x, np.ndarray):
        x = x.tolist()
        print("X: ",x)
    else:
        x = [float(x)]
        print("X:", x)



    dataFile = "src/GPD/data/"+analysisVariables[0]+"/E/"+analysisVariables[1]+".csv"
    flavourKeyList = analysisVariables[5]
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]
    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) # returns a dict: dict["flavours"] = [aprime,B,A]

    results = {}
    for flavours in flavourKeyList:
        parameters = paramterDict[flavours]
        results[flavours] = computationHandeler(parameters, x)

    print("results:",results )
    print("################################")
    return results

    


