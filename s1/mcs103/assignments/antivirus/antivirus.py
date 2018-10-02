import os
import argparse
import glob
import numpy as np

def main():
    #define argument parser with path and optional extension
    parser = argparse.ArgumentParser(description = 'SAM antivirus')
    parser.add_argument('path', help = 'Absolute Path of the directory')
    parser.add_argument('-e', '--extension', default = '', help = 'File extension to filter by')
    args = parser.parse_args()

    #exit if path is not defined
    if not os.path.isdir(args.path):
        print("Enter a valid path")
        exit(1)
   
    #create a set of files in that path
    path = args.path
    files = set()
    files |= set(glob.glob(path + '/*' + args.extension))

    #randomly display file as virus or not
    virus = set()
    for file in files:
        chance = np.random.rand()
        if(chance > 0.3):
            print("\033[92m✔", file)
        else:
            virus.add(file)
            print("\033[91m✘", file)
   
    if virus:
        print("\n\033[0;34mCheck Complete - Files with virus are:")
        for file in virus:
            print("\033[91m✘", file)
    else:
        print("\n\033[0;34mCheck Complete - No viruses found!!")

if __name__ == "__main__":
    main()
