import os
import requests
import pandas as pd
from sortedcontainers import SortedDict

import csv

def get_dataframe(fname):
    df = pd.read_excel(fname)
    return df

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Species Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )

def Combine(df1,df2,df3):
    genus = SortedDict()
    for index, row in df1.iterrows():
        genusVal = str(row['ScientificName'])
        AphiaID = str(row['AphiaID'])
        Match_type = str(row['Match type'])

        genus[genusVal] = (AphiaID,Match_type)

    for index, row in df2.iterrows():
        genusVal = str(row['ScientificName'])
        AphiaID = str(row['AphiaID'])
        Match_type = str(row['Match type'])
        genus[genusVal] = (AphiaID,Match_type)

    for index, row in df3.iterrows():
        genusVal = str(row['ScientificName'])
        AphiaID = str(row['AphiaID'])
        Match_type = str(row['Match type'])

        genus[genusVal] = (AphiaID,Match_type)


    return genus

def call_get_REST(genusSortedDict):
    genus = SortedDict()
    for genusVal in genusSortedDict:
        (AphiaID, Match_type)=  genusSortedDict[genusVal]
        if AphiaID == 'nan':
            continue
        AphiaID = str(int(float(AphiaID)))
        print(AphiaID)
        api_url = 'https://www.marinespecies.org/rest/AphiaChildrenByAphiaID/'+ AphiaID +'?marine_only=false&offset=1'
        try:
            response = requests.get(api_url)
            r = response.json()
            s= response.status_code
            species_cnt= len(r)
            genus[genusVal] = species_cnt
        except:
            genus[genusVal] = 0
    return genus

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Species Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )

def main():
    fname1 = '../WoRMS/submission_001_matched.xlsx'
    fname2 = '../WoRMS/submission_002_matched.xlsx'
    fname3 = '../WoRMS/submission_003_matched.xlsx'


    df1 = get_dataframe(fname1)
    df2 = get_dataframe(fname2)
    df3 = get_dataframe(fname3)

    genusDic = Combine(df1,df2,df3)
    print(genusDic)
    genusDic = call_get_REST(genusDic)

    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genusDic)

if __name__ == '__main__':
    main()
