import cv2
import numpy as np
import glob
import os


def get_file_list(thisdir):
    lst = []
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".jpg"):
                # print(os.path.join(r, file))
                lst.append(os.path.join(r, file))
    return lst



def main(lst, name, outDir):
    img_array = []

    size = (0, 0)
    for filename in lst:
        print("filename--->")
        print(filename)
        img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

        print('Original Dimensions : ', img.shape)

        ''' width = 2448
        height = 3264
        dim = (width, height)

        # resize image
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        '''

        height, width, layers = img.shape
        size = (width, height)

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0, 0, 0)
        thickness = 2

        org = (10, 100)
        # name = 'Nem_02'
        #img = cv2.putText(img, name, org, font,
        #                  fontScale, color, thickness, cv2.LINE_AA)

        img_array.append(img)
    # name = 'Nem_02'
    outFile = outDir + name
    out = cv2.VideoWriter(outFile + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

    for i in range(len(img_array)):
        out.write(img_array[i])

    out.release()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nem_name = 'Xhygro.bulb1'
    dir = 'D:/Nemalogic_Git_Hub/nemalogic/nemalogic.github.io/img/Glossary/Video Xiphinema hygrophilum/Xhygro.bulb1/'
    outDir = 'D:/Nemalogic_Git_Hub/nemalogic/nemalogic.github.io/img/Glossary/Video Xiphinema hygrophilum/Xhygro.bulb1/'
    lst = get_file_list(dir)
    print(lst)
    main(lst, nem_name, outDir)