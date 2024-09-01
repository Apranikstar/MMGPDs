import numpy as np


def computeH(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
        print("t: ",t)
    else:
        t = [float(t)]
        print("t:", t)
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    resultDict = {}
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
        resultDict[flavour]=resultList
      
    # Convert lists to numpy arrays for element-wise addition
    if ("uv" in resultDict) and ("ubar" in resultDict):
        resultDict["u"] = np.array(resultDict["uv"]) + np.array(resultDict["ubar"])
    if ("dv" in resultDict) and ("dbar" in resultDict):
        resultDict["d"] = np.array(resultDict["dv"]) + np.array(resultDict["dbar"])
    if ("sv" in resultDict) and ("sbar" in resultDict):
        resultDict["s"] = np.array(resultDict["sv"]) + np.array(resultDict["sbar"])

    # Convert arrays back to lists (if necessary)
    #for key in resultDict:
    #    resultDict[key] = resultDict[key].tolist()

    print("H GPD = \n ", resultDict)
    return resultDict
    

def computeHt(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
        print("t: ",t)
    else:
        t = [float(t)]
        print("t:", t)
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    resultDict = {}
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
        resultDict[flavour]=resultList
    # Convert lists to numpy arrays for element-wise addition
    if ("uv" in resultDict) and ("ubar" in resultDict):
        resultDict["u"] = np.array(resultDict["uv"]) + np.array(resultDict["ubar"])
    if ("dv" in resultDict) and ("dbar" in resultDict):
        resultDict["d"] = np.array(resultDict["dv"]) + np.array(resultDict["dbar"])
    if ("sv" in resultDict) and ("sbar" in resultDict):
        resultDict["s"] = np.array(resultDict["sv"]) + np.array(resultDict["sbar"])

    # Convert arrays back to lists (if necessary)
    #for key in resultDict:
    #    resultDict[key] = resultDict[key].tolist()

    print("Ht GPD = \n ", resultDict)
    return resultDict


def computeE(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
        print("t: ",t)
    else:
        t = [float(t)]
        print("t:", t)
    if isinstance(flavourslist,str):
        flavourslist = [flavourslist]
        
    resultDict = {}
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
        resultDict[flavour]=resultList
    # Convert lists to numpy arrays for element-wise addition
    if ("uv" in resultDict) and ("ubar" in resultDict):
        resultDict["u"] = np.array(resultDict["uv"]) + np.array(resultDict["ubar"])
    if ("dv" in resultDict) and ("dbar" in resultDict):
        resultDict["d"] = np.array(resultDict["dv"]) + np.array(resultDict["dbar"])
    if ("sv" in resultDict) and ("sbar" in resultDict):
        resultDict["s"] = np.array(resultDict["sv"]) + np.array(resultDict["sbar"])

    # Convert arrays back to lists (if necessary)
    #for key in resultDict:
    #    resultDict[key] = resultDict[key].tolist()

    print("Ht GPD = \n ", resultDict)
    return resultDict