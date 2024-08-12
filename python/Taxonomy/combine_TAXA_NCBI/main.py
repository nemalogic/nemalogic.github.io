import os

import pandas as pd
from sortedcontainers import SortedDict

import csv

def get_dataframe(fname):
    df = pd.read_csv(fname)
    return df

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Species Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )

def Combine(ncbiDf,zootaxaDf):
    genus = SortedDict()
    for index, row in ncbiDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0,0)

    for index, row in zootaxaDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0, 0)

    for index, row in ncbiDf.iterrows():
        genusVal = str(row['Genus'])
        spCnt = row['Species Count']
        genus[genusVal] = (spCnt,0)

    for index, row in zootaxaDf.iterrows():
        genusVal = str(row['Genus'])
        spCnt = row['Species Count']
        (first, second) = genus[genusVal]
        genus[genusVal] = (first, spCnt)

    return genus

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'NCBI Species Count' + ',' + 'TAXA Species Count' + '\n')
        for line in genus:
            (NCBI, TAXA) = (genus[line])
            f.write( line + ',' + str(NCBI)  + ',' +  str(TAXA) + '\n' )

def main():
    fname1 = '../ParseNCBIData/txtFile.csv'
    fname2 = '../ParseZooTaxaPdf/txtFile.csv'


    ncbiDf = get_dataframe(fname1)
    zootaxaDf = get_dataframe(fname2)

    genusdf = Combine(ncbiDf,zootaxaDf)
    print(genusdf)
    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genusdf)

if __name__ == '__main__':
    main()
