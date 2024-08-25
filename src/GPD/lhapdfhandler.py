import subprocess
import os
import lhapdf


def GetLHAPDF():
    print("Make sure you have LHAPDF installed.")
    print("Looking for PDFSETS Directory \n")
    # Run the command and capture the output
    path = subprocess.check_output(['lhapdf-config', '--datadir'], text=True).strip()
    # Print the output to verify
    if path:
        print("The path to your PDF sets is: " + path+ "\n")
    else:
        raise Exception("Intentional Crash, could not run lhapdf-config --datadir \n")
    all_items = os.listdir(path)
    print( all_items)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    print("Successfuly retrieved LHAPDF! \n")
    print("################################")
    print("You have the following PDF sets:")
    print(directories)
    lhapdf.setPaths(path)  
    LHAPDF = [path , directories]
    return LHAPDF


def GetAnalysisUPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDF40_nlo_as_01180",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("CT10nlo",0)

def GetAnalysisPPDF(AnalysisType):
    if AnalysisType == "HGAG23":
        return lhapdf.mkPDF("NNPDFpol11_100",0)
    if AnalysisType == "Analysis2":
        return lhapdf.mkPDF("CT10nlo",0)



