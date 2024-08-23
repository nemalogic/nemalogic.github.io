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

def Combine(ncbiDf,zootaxaDf,wormsDf,genBankDf):
    genus = SortedDict()
    for index, row in ncbiDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0,0,0,0)

    for index, row in zootaxaDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0,0,0,0)

    for index, row in wormsDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0,0,0,0)

    for index, row in genBankDf.iterrows():
        genusVal = str(row['Genus'])
        genus[genusVal] = (0,0,0,0)


    for index, row in ncbiDf.iterrows():
        genusVal = str(row['Genus'])
        (first, second, third, fourth) = genus[genusVal]
        first = row['Species Count']
        genus[genusVal] = (first,0,0,0)

    for index, row in zootaxaDf.iterrows():
        genusVal = str(row['Genus'])
        second = row['Species Count']
        (first, second, third, fourth) = genus[genusVal]
        second = row['Species Count']
        genus[genusVal] = (first, second, third,fourth)

    for index, row in wormsDf.iterrows():
        genusVal = str(row['Genus'])
        (first, second,third,fourth) = genus[genusVal]
        third = row['Species Count']
        genus[genusVal] = (first, second,third,fourth)

    for index, row in genBankDf.iterrows():
        genusVal = str(row['Genus'])
        (first, second,third,fourth) = genus[genusVal]
        fourth = row['Sequence Count']
        genus[genusVal] = (first, second,third,fourth)

    return genus

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'NCBI Species Count' + ',' + 'TAXA Species Count' + ',' + 'WoRMS Species Count' + ',' + 'GenBank Sequence Count''\n')
        for line in genus:
            (NCBI, TAXA, WoRMS, GenBank) = (genus[line])
            f.write( line + ',' + str(NCBI)  + ',' +  str(TAXA) + ',' +  str(WoRMS) + ',' +  str(GenBank) + '\n' )

def main():
    fname1 = '../ParseNCBIData/txtFile.csv'
    fname2 = '../ParseZooTaxaPdf/txtFile.csv'
    fname3 = '../ParseWoRMS/txtFile.csv'
    fname4 = '../GenBank/CountSequences/txtFile.csv'


    ncbiDf = get_dataframe(fname1)
    zootaxaDf = get_dataframe(fname2)
    wormsDf = get_dataframe(fname3)
    genBankDf = get_dataframe(fname4)

    genusdf = Combine(ncbiDf,zootaxaDf,wormsDf,genBankDf)
    print(genusdf)
    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genusdf)

if __name__ == '__main__':
    main()