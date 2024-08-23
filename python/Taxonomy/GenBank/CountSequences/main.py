import os
import requests
import pandas as pd
from sortedcontainers import SortedDict

import csv


def get_fasta_files():
    thisdir = '../GetSequences'
    fasta_files = []
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".fasta"):
                #print(os.path.join(r, file))
                file = os.path.join(r, file)
                fasta_files.append(file)
    return fasta_files

def parse_fasta_files(fasta_files):
    lines = list()
    descrpitionLst = list()
    for f in fasta_files:
        print (f)
        with open(f) as fastaFile:
            lines = fastaFile.readlines()
        for l in lines:
            if l[0] == '>' :
                descrpitionLst.append(l)
    return descrpitionLst

def get_Genus_Name(descrpitionLst):
    genus = SortedDict()
    lines = list()
    for d in descrpitionLst:
        sss = d.split()
        g = sss[1]
        if g in genus:
            genus[g] = genus[g] + 1
        else:
            genus[g] = 1
    return genus



def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Sequence Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )


def main():
    fasta_files = get_fasta_files()
    descrpitionLst = parse_fasta_files(fasta_files)
    genusDic = get_Genus_Name(descrpitionLst)

    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genusDic)

if __name__ == '__main__':
    main()
