import numpy as np


#############  Subroutines  #############
def _uv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(2,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-2,items,np.sqrt(Q2)))
    return results
def _dv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(1,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-1,items,np.sqrt(Q2)))
    return results
def _sv(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(3,items,np.sqrt(Q2)) - analysisPDFSET.xfxQ(-3,items,np.sqrt(Q2)))
    return results
def _ubar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(2,items,np.sqrt(Q2)) )
    return results
def _dbar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(1,items,np.sqrt(Q2)))
    return results
def _sbar(x,analysisPDFSET,Q2):
    results = []
    for items in x:
        results.append(analysisPDFSET.xfxQ(3,items,np.sqrt(Q2)) )
    return results
    #######################################



def _PDF(x,Q2, flavourList, analysisPDFSET):
    print("####################Calculating PDF at Forward Limits###################")
    if isinstance(x, np.ndarray):
        x = x.tolist()
        print("X: ",x)
    else:
        x = [float(x)]
        print("X:", x)
    if isinstance(Q2, np.ndarray):
        Q2 = Q2.tolist()
        print("Q2: ",Q2)
    else:
        Q2 = float(Q2)
        print("Q2: ",Q2)

    results = {}
    for flavour in flavourList:
        if flavour == "uv":
            results["uv"] = _uv(x,analysisPDFSET,Q2)
        elif flavour == "dv":
            results["dv"] = _dv(x,analysisPDFSET,Q2) 
        elif flavour == "sv":
            results["sv"] = _sv(x,analysisPDFSET,Q2)
        elif flavour =="ubar":
            results["ubar"] =  _ubar(x,analysisPDFSET,Q2)
        elif flavour =="dbar":
            results["dbar"]= _dbar(x,analysisPDFSET,Q2)
        elif flavour =="sbar":
            results["sbar"]=  _sbar(x,analysisPDFSET,Q2)
    print("####################PDF Calculated Successfuly!###################")

    return results
        
