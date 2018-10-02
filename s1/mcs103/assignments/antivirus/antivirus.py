import os
import argparse
import glob
import virus_checker as vc
import sys

def main():
    #define argument parser with path and optional extension
    parser = argparse.ArgumentParser(description = 'SAM antivirus')
    parser.add_argument('path', nargs = "?", default = os.getcwd(), help = 'Absolute Path of the directory')
    parser.add_argument('-e', '--extension', nargs = "+",  default = [""], help = 'File extension to filter by')
    args = parser.parse_args()

    #exit if path is not defined
    if not os.path.isdir(args.path):
        print("Enter a valid path")
        exit(1)
   
    #create a set of files that are in the defined path
    path = args.path
    files = set()
    for arg in args.extension:
        contents = glob.glob(path + '/*' + arg)
        contents = [content for content in contents if os.path.isfile(content)]
        files |= set(contents)

    #randomly display file as virus or not
    virus = set()
    for file in files:
        sys.stdout.write("\033[0mrunning...")
        sys.stdout.flush()
        FileIsVirus = vc.isVirus(file)
        sys.stdout.write('\r')
        if(FileIsVirus):
            print("\033[92m✔", file)
        else:
            virus.add(file)
            print("\033[91m✘", file)
        
    if virus:
        print("\n\033[0;34mCheck Complete - Files with virus are:")
        for file in virus:
            print("\033[91m✘", os.path.basename(file))
    else:
        print("\n\033[0;34mCheck Complete - No viruses found!!")

if __name__ == "__main__":
    main()
