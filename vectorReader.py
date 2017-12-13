import simpleVector
from pprint import pprint as pp
def loadVectors(fileName):
    try:
        with open(fileName, 'r') as mf:
            lines = mf.readlines()
    except:
        return None
    vectors = []
    for line in lines:
        try:
            vectors.append(simpleVector.Vector(line.strip()))
        except:
            vectors.append(None)
    return vectors

def printVectors(vectors):
    for vector in vectors:
        if not vector:
            print(vector)
            continue
        print("{}, {}".format(vector.x, vector.y))

if __name__ == "__main__":
    l = loadVectors('values.txt')
    print(l)
    # printVectors(l)