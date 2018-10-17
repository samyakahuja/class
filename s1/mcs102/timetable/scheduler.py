## main file - import logic + AI

import argparse
import os
import csv
import pandas as pd

def initialize():
    parser = argparse.ArgumentParser(description = 'TimeTable Scheduler')
    parser.add_argument('path', default = "", help = 'Absolute path to the file')
    args = parser.parse_args()

    path = args.path
    if not os.path.isfile(path):
        print("Not a valid file path!")
        exit(1)
    fileName, fileExtension = os.path.splitext(path)
    if not fileName or fileExtension != ".csv":
        print(os.path.basename(path), "is not a csv")
        exit(1)

    df = pd.read_csv(path)
    print(df)

if __name__ == "__main__":
    initialize()
