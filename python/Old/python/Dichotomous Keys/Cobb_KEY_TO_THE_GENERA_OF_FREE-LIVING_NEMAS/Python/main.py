# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
import pandas as pd
import openpyxl

def readSpreadSheet():
    fn = 'X:/var/www/WKW_001/python/Dichotomous Keys/Cobb_KEY_TO_THE_GENERA_OF_FREE-LIVING_NEMAS/Book1.xlsx'
    df = pd.read_excel(fn, sheet_name='Book1')
    df = df.fillna('')
    return df

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str



def draw(df):
    #http://nemaplex.ucdavis.edu/Uppermnus/nematamnu.htm#Taxonomic_Keys
    #http://nemaplex.ucdavis.edu/Taxadata/Tylenchidaekey2008.htm
    GraphTitle = 'Cobb\nKEY TO THE GENERA\nOF\nFREE-LIVING_NEMAS'
    g = Digraph('GraphTitle', comment="FOO",filename = 'NematodaKey.gv') #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g.graph_attr['rankdir'] = 'LR'
    g.attr(label=GraphTitle)

    g.node('000', label=GraphTitle,fillcolor='red',style="filled")
    g.edge('000', '001', label2(''))

    cnt=0
    for index, row in df.iterrows():
        KeyFrom = str(row['KeyFrom'])
        KeyTo = str(row['KeyTo']).strip()


        if KeyTo.isdigit():
            KeyTo = KeyTo.zfill(3)
        if KeyFrom.isdigit():
            KeyFrom = KeyFrom.zfill(3)

        Description = str(row['Edge']).strip()
        if len(Description) < 2:
            continue
        #g.node(KeyFrom, KeyTo,fillcolor='aqua',style="filled" )
        g.edge(KeyFrom,KeyTo, label2(Description))
        if cnt > 60:
          break
        cnt = cnt +1


    g.render('NematodaKey.gv', format='svg', view=True)
    #g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)


    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label2('')
    #g.edge('','', label2('')


def main():
    # Use a breakpoint in the code line below to debug your script.
    df = readSpreadSheet()
    draw(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
