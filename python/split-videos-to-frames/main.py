import os
import numpy as np
import argparse
import cv2


def main():
    # parse all args
    #parser = argparse.ArgumentParser()
    #parser.add_argument('source', type=str, help='Path to source video')
    #parser.add_argument('dest_folder', type=str, help='Path to destination folder')
    #args = parser.parse_args()

    # get file path for desired video and where to save frames locally
    source = 'D:/Nemalogic_Git_Hub/nemalogic/nemalogic.github.io/img/Glossary/Video Xiphinema hygrophilum/Xhygro.lipregion1.6x.mov'        #args.source
    dest_folder = 'D:/Nemalogic_Git_Hub/nemalogic/nemalogic.github.io/img/Glossary/Video Xiphinema hygrophilum/Xhygro.lipregion1.6x'   #args.dest_folder
    cap = cv2.VideoCapture(source)
    path_to_save = os.path.abspath(dest_folder)

    current_frame = 1

    if (cap.isOpened() == False):
        print('Cap is not open')

    # cap opened successfully
    while (cap.isOpened()):

        # capture each frame
        ret, frame = cap.read()
        if (ret == True):

            # Save frame as a jpg file
            name = 'frame' + str(current_frame).zfill(3) + '.jpg'
            print(f'Creating: {name}')
            cv2.imwrite(os.path.join(path_to_save, name), frame)

            # keep track of how many images you end up with
            current_frame += 1

        else:
            break

    # release capture 
    cap.release()
    print('done')


if __name__ == '__main__':
    main()