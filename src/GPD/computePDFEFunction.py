import numpy as np
from scipy.integrate import quad
import csv
import src.GPD.csvdataparser as csvdataparser

# Define the function to integrate
def integrand(x, alpha_q, beta_q, gamma_q):
    return (np.power(x, -alpha_q) * np.power(1-x, beta_q) * (1 + gamma_q * np.sqrt(x)))


def ComputePDFEFunction(analysisVariables, x):
    k={}
    k["uv"]=1.67
    k["dv"]=-2.03

    dataFile = "src/GPD/data/"+analysisVariables[0]+"/E/"+analysisVariables[1]+".csv"
    flavourKeyList = analysisVariables[5]
    if isinstance(flavourKeyList,str):
        flavourKeyList = [flavourKeyList]

    paramterDict = csvdataparser.get_flavour_values(dataFile, flavourKeyList) 
    alpha= {}
    beta = {}
    gamma = {}
    for flavours in flavourKeyList:
        alpha[flavours] = paramterDict[flavours][3] #alpha
        beta[flavours]= paramterDict[flavours][4] #beta
        gamma[flavours] = paramterDict[flavours][5] # gamma for "uv"

    N = {}
    for flavours in flavourKeyList:
        Nitem , error = quad(integrand, 0, 1, args=(alpha[flavours], beta[flavours], gamma[flavours]))
        N[flavours] = np.divide(1,Nitem)
    print("Normalization Factors are: ", N)

    E = {}
    for flavours in flavourKeyList: # note that we added a x to make the final results xE[flavour]
        E[flavours] = x * k[flavours] * N[flavours]  * np.power(x,-alpha[flavours]) * np.power(1-x,beta[flavours]) * (1+ gamma[flavours] * np.sqrt(x))
    print("GPD E is equal to: ")
    return E