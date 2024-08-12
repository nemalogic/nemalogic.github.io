import os

import pypdfium2 as pdfium
#https://github.com/pypdfium2-team/pypdfium2

import csv

def get_Text(fname):
    pdf = pdfium.PdfDocument(fname)
    version = pdf.get_version()  # get the PDF standard version
    n_pages = len(pdf)  # get the number of pages in the document
    page = pdf[0]  # load a page
    text = []
    for page in pdf:
        textpage = page.get_textpage()
        text_all = textpage.get_text_range()
        lines = text_all.splitlines()
        for line in lines:
            if len(line.strip()) > 1:
                text.append(line)
    return text

def PrintDictToFile(fn, genus):
    with open(fn, 'w',encoding="utf-8",newline='') as f:
        f.write('Genus' + ',' + 'Species Count' + '\n')
        for line in genus:
            f.write( line + ',' + str(genus[line]) + '\n' )

def GetTaxonomy(text):
    genus = dict()
    for line in text:
        print(line)
        if 'Genus' in line:
            strings = line.split()
            if 'species' in line:
                if '(' in line:
                    sp = line.split('(')
                    if len(sp) > 2:
                        sp2 = sp[2]
                    else:
                        sp2 = sp[1]
                        sp3 = sp2.split()
                    print(sp2)
                    genus[strings[1]] = int(sp3[0])
            else:
                genus[strings[1]] = 0
            print(genus[strings[1]])
    return genus

def main():
    fname = '../ZOOTAXA/45351-Article Text-48185-51986-10-20220310.pdf'
    fd = open(fname, "rb")
    textPage = get_Text(fname)
    #print (textPage)
    #txtFile = 'txtFile.txt'
    #PrintLstToFile(txtFile, textPage)
    genus = GetTaxonomy(textPage)
    txtFile = 'txtFile.csv'
    PrintDictToFile(txtFile, genus)

if __name__ == '__main__':
    main()
