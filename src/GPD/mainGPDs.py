import lhapdf
import src.GPD.lhapdfhandler as lhapdfhandler
import numpy as np
import src.GPD.analysishandler as analysishandler
import time
import uncertainties
import src.GPD.csvdataparser as csvdataparser
import src.GPD.datapointshandler as dp
import src.GPD.computePDFFunction as computePDFFunction
import src.GPD.computeProfFunc as computeProfFunc
import src.GPD.computeHGPD as computeHGPD
import src.GPD.csvOutputHandler as csvOutputHandler

################# 
def GPDMethod():
    print("Initializing MMGPD toolchain.")
    systemPDFINFO = lhapdfhandler.GetLHAPDF() # is a list of [path,directories]
    ################# 
    analysisVariables = analysishandler.GetAnalysisParameters() # Returns ["Analysis", "GPDs set","GPD to calc", [Flavour List] ]
    ### ADD GPD TYPE
    ################# 
    analysisPDFSET = lhapdfhandler.GetAnalysisPDF(analysisVariables[0]) # Returns lhapdf.mkPDF("AnalysisSpecificPDF",0)
    #################
    analysisDataPoints = dp.GetDataPoints() # x , Q2 , t
    ################
    # Calculating pdf function q()
    pdfFunction = computePDFFunction._PDF(analysisDataPoints[0],analysisDataPoints[1], analysisVariables[3], analysisPDFSET)
    print("PDF at forward limit is:", pdfFunction) #pdfFunction returns a dictionary of flavours "uv", "dv",etc
    print("################")
    ################
    # Calculating Profile Function f()
    profileFunction = computeProfFunc._profileFunc( analysisVariables, analysisDataPoints[0])
    print("Profile Function was Successfully Calculated ")
    ################
    # computeH(pdfFunction, profileFunction, t, flavourslist)
    H = computeHGPD.computeH(pdfFunction, profileFunction, analysisDataPoints[2],analysisVariables[3])
    ################
    csvOutputHandler.save_dict_to_csv(pdfFunction, "pdfFunction.csv")
    csvOutputHandler.save_dict_to_csv(profileFunction, "profileFunctions.csv")
    csvOutputHandler.save_dict_to_csv(H, "H.csv")
    csvOutputHandler.write_list_to_csv(analysisDataPoints,"DataPointsX.csv")
    print("Data are stored in /outputs/Rawdata\n")

    ##### Note that for our line of work we need Q2 and t to be constant and x to be the variable.
    ## WRITE A PRINT TO TO CITE THE CORRESPONDING PAPERS
    # Get Kinematic points singular or multiple
    # calculate _PDF 
    # calculate profile function
    #calculate GPDs
    print("################################")
    time.sleep(5)
    print("################Closed properly################")

