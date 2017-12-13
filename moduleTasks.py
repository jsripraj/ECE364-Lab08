from exModule import runNetworkCode
import re
from pprint import pprint as pp

def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except OSError as e:
        if type(e) == ConnectionError:
            raise
        return "An issue encountered during runtime. The name of the error is: {}".format(type(e).__name__)
    except:
        return False
    else:
        return True
def isOK(signalName):
    if re.match('^[A-Z]{3}-[0-9]{3}$', signalName):
        return True
    return False
def loadDataFrom(signalName, folderName):
    if not isOK(signalName):
        raise ValueError("{} is invalid.".format(signalName))
    try:
        with open(folderName + '/' + signalName + '.txt', 'r') as mf:
            lines = mf.readlines()
    except:
        raise OSError("{}.txt is not present in {}.".format(signalName, folderName))
    valid = []
    invalid = 0
    for data in lines:
        if re.match('^-?[0-9]+.[0-9]+$', data):
            valid.append(data.strip())
        else:
            invalid += 1
    return (valid, invalid)
def isBounded(signalValues, bounds, threshold):
    if not signalValues:
        raise ValueError("Signal contains no data.")
    min, max = bounds
    invalid = [value for value in signalValues if float(value) > max or float(value) < min]
    if len(invalid) <= threshold:
        return True
    return False
if __name__ == "__main__":
    a = checkNetwork(osError=1, connectionError=0, otherError=0, noError=1)
    b = isOK('AFW--489')
    c = loadDataFrom('CIG-308', 'Signals')
    valid, invalid = c
    d = isBounded(valid, (-12.95, 12.95), 50)
