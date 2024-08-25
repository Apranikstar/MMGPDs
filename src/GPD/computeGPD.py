import numpy as np


def computeH(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
        print("t: ",t)
    else:
        t = [float(t)]
        print("t:", t)

    resultDict = {}
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
        resultDict[flavour]=resultList
    print("H GPD = \n ", resultDict)
    return resultDict

    

def computeHt(pdfFunction, profileFunction, t, flavourslist):
    if isinstance(t, np.ndarray):
        t = t.tolist()
        print("t: ",t)
    else:
        t = [float(t)]
        print("t:", t)

    resultDict = {}
    for flavour in flavourslist:
        resultList = []
        for i in range(len(pdfFunction[flavour])):
            resultList.append(pdfFunction[flavour][i] * np.exp(t[0] * profileFunction[flavour][i]))
        resultDict[flavour]=resultList
    print("H GPD = \n ", resultDict)
    return resultDict