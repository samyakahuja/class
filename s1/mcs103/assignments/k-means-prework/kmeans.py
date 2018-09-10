import numpy as np

def load_dataset(name):
    return np.loadtxt(name)

# Data Definition
# Col1: Average data sent by user per hour.
# Col2: Avearge file size of data sent by user.

def euclidean(a,b):
    # returns L-2 norm
    return np.linalg.norm(a-b)

def kmeans(k):
    print('kmeans',k)

def main():
    dataset = load_dataset('data.txt')
    print(dataset)
    #centroids, clusters = kmeans(2)
    kmeans(10)

if __name__ == '__main__':
    main()
