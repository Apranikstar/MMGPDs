import lhapdf
import src.GPD.lhapdfhandler as lhapdfhandler
import numpy as np
import src.GPD.analysishandler as analysishandler
import time
import uncertainties
import src.GPD.csvdataparser as csvdataparser
import src.GPD.datapointshandler as dp
import src.GPD.computePDFFunction as computePDFFunction
################# 
def GPDMethod():
    print("Initializing MMGPD toolchain.")
    systemPDFINFO = lhapdfhandler.GetLHAPDF() # is a list of [path,directories]
    ################# 
    analysisVariables = analysishandler.GetAnalysisParameters() # Returns ["Analysis", "GPDs set", [Flavour List] ]
    ### ADD GPD TYPE
    ################# 
    analysisPDFSET = lhapdfhandler.GetAnalysisPDF(analysisVariables[0]) # Returns lhapdf.mkPDF("AnalysisSpecificPDF",0)
    #################
    analysisDataPoints = dp.GetDataPoints()
    ################
    pdfFunction = computePDFFunction._PDF(analysisDataPoints[0],analysisDataPoints[1], analysisVariables[3], analysisPDFSET)
    print("PDF at forward limit is:", pdfFunction) #pdfFunction returns a dictionary of flavours "uv", "dv",etc

    ##### Note that for our line of work we need Q2 and t to be constant and x to be the variable.
    ## WRITE A PRINT TO TO CITE THE CORRESPONDING PAPERS
    # Get Kinematic points singular or multiple
    # calculate _PDF 
    # calculate profile function
    #calculate GPDs
    print("################################")
    time.sleep(5)
    print("################Closed properly################")

