import os

import pandas as pd
#https://github.com/pypdfium2-team/pypdfium2

import csv

def get_Text(fname):
    df = pd.read_csv(fname, sep='\t')
    df1 = df.loc[df['Rank'] == 'SPECIES']
    df2 = df1[['Tax name']]
    return df2

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Species Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )

def GetTaxonomy(df):
    genus = dict()
    for index, row in df.iterrows():
        genusVal = str(row['Tax name']).split()
        print (genusVal[0])
        if genusVal[0] in genus:
            genus[genusVal[0]] = genus[genusVal[0]] + 1
        else:
            genus[genusVal[0]] = 1
    return genus

def main():
    fname = '../NCBI/command_line_tools/ncbi_dataset/ncbi_dataset/data/taxonomy_summary.tsv'


    genusdf = get_Text(fname)
    genusdf = GetTaxonomy(genusdf)
    print(genusdf)
    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genusdf)

if __name__ == '__main__':
    main()
