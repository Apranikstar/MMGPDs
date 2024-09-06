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
import src.GPD.computeGPD as computeGPD
import src.GPD.csvOutputHandler as csvOutputHandler
import src.GPD.plotHandler as plotHandler
import src.GPD.computePDFEFunction as computePDFEFunction

################# 
def GPDMethod():
    print("Initializing MMGPD toolchain.")
    systemPDFINFO = lhapdfhandler.GetLHAPDF() # is a list of [path,directories]
    ################# 
    analysisVariables = analysishandler.GetAnalysisParameters() # Returns ["Analysis", "GPDs set","GPD to calc", [Flavour List] ]
    
    analysisDataPoints = dp.GetDataPoints() # x , Q2 , t
    ################
    if "H" in analysisVariables[2]:
        analysisUPDFSET = lhapdfhandler.GetAnalysisUPDF(analysisVariables[0]) # Returns lhapdf.mkPDF("AnalysisSpecificPDF",0)
        pdfHFunction = computePDFFunction._PDF(analysisDataPoints[0],analysisDataPoints[1], analysisVariables[3], analysisUPDFSET)
        profileHFunction = computeProfFunc._profileFuncH( analysisVariables, analysisDataPoints[0])
        H = computeGPD.computeH(pdfHFunction, profileHFunction, analysisDataPoints[2],analysisVariables[3])
        csvOutputHandler.save_dict_to_csv(pdfHFunction, "pdfHFunction.csv")
        csvOutputHandler.save_dict_to_csv(profileHFunction, "profileHFunction.csv")
        csvOutputHandler.save_dict_to_csv(H, "H.csv")
        
        if isinstance(analysisDataPoints[0],str):
            pass
        else:
            csvOutputHandler.write_list_to_csv(analysisDataPoints[0],"DataPointsX.csv")
            plotHandler.plot_and_save("outputs/Rawdata/DataPointsX.csv","outputs/Rawdata/H.csv", "H",analysisDataPoints[2] ,output_dir='outputs/plots/H')
        






    # Check for analysis variables for each GPD
    if "Ht" in analysisVariables[2]:
        analysisPPDFSET = lhapdfhandler.GetAnalysisPPDF(analysisVariables[0]) # Returns lhapdf.mkPDF("AnalysisSpecificPDF",0)
        pdfHtFunction = computePDFFunction._PDF(analysisDataPoints[0],analysisDataPoints[1], analysisVariables[4], analysisPPDFSET)
        profileHtFunction = computeProfFunc._profileFuncHt( analysisVariables, analysisDataPoints[0])
        Ht = computeGPD.computeHt(pdfHtFunction, profileHtFunction, analysisDataPoints[2],analysisVariables[4])
        csvOutputHandler.save_dict_to_csv(pdfHtFunction, "pdfHtFunction.csv")
        csvOutputHandler.save_dict_to_csv(profileHtFunction, "profileHtFunction.csv")
        csvOutputHandler.save_dict_to_csv(Ht, "Ht.csv")
        
        if isinstance(analysisDataPoints[0],str):
            pass
        else:
            csvOutputHandler.write_list_to_csv(analysisDataPoints[0],"DataPointsX.csv")
            plotHandler.plot_and_save("outputs/Rawdata/DataPointsX.csv","outputs/Rawdata/Ht.csv", "Ht" , analysisDataPoints[2], output_dir='outputs/plots/Ht', )
        




### ADD A LINE TO CHECK IF DATAPOINT X EXISTS 


    if "E" in analysisVariables[2]:
        profileEFunction = computeProfFunc._profileFuncE( analysisVariables, analysisDataPoints[0])
        pdfEFunction = computePDFEFunction.ComputePDFEFunction(analysisVariables, analysisDataPoints[0])
        E = computeGPD.computeE(pdfEFunction, profileEFunction, analysisDataPoints[2],analysisVariables[5])
        csvOutputHandler.save_dict_to_csv(pdfEFunction, "pdfEFunction.csv")
        csvOutputHandler.save_dict_to_csv(profileEFunction, "profileEFunction.csv")
        csvOutputHandler.save_dict_to_csv(E, "E.csv")
        
        if isinstance(analysisDataPoints[0],str):
            pass
        else:
            csvOutputHandler.write_list_to_csv(analysisDataPoints[0],"DataPointsX.csv")
            plotHandler.plot_and_save("outputs/Rawdata/DataPointsX.csv","outputs/Rawdata/E.csv", "E",analysisDataPoints[2] ,output_dir='outputs/plots/E' )
        

        
    print("All Calculations due to the following analysis \n: ", analysisVariables , "\n is complete!")
    print("Q2= ", analysisDataPoints[1], "t = ", analysisDataPoints[2])
    print("Data are stored in /outputs/Rawdata\n /outputs/plots")
    print("################################")
    print("################Closed properly################")

