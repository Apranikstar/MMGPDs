from src.GPD import mainGPDs as gpd
from src.PDF import mainPDFs as pdf

def main():
    start = input("To use PDFs write: PDF \n To use GPDs write: GPD \n ")

        if start == "PDF":
            pdf.PDFMethods()
        elif start == "GPD":
            gpd.GPDMethod()
        else:
            main()

if __name__ == "__main__":
    main()

