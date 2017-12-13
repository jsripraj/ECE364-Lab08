import moduleTasks
from pprint import pprint as pp
def loadMultiple(signalNames, folderName, maxCount):
    signalValueDict = {}
    for signalName in signalNames:
        try:
            data = moduleTasks.loadDataFrom(signalName, folderName)
        except:
            signalValueDict[signalName] = None
        else:
            valid, invalid = data
            if invalid <= maxCount:
                signalValueDict[signalName] = valid
            else:
                signalValueDict[signalName] = []
    return signalValueDict
def saveData(signalsDictionary, targetFolder, bounds, threshold):
        for signalName, valuesList in signalsDictionary.items():
            try:
                moduleTasks.isBounded(valuesList, bounds, threshold)
            except ValueError:
                continue
            else:
                with open(targetFolder + '/' + signalName + '.txt', 'w') as mf:
                    for value in valuesList:
                        mf.write('{0:.3f}\n'.format(float(value)))
if __name__ == "__main__":
    a = loadMultiple(['XZC-901', 'AFW-481', 'XDF-846', 'CIG-308', 'GUO-758'], 'Signals', 50)
    saveData(a, 'testDir', (-6.0, 6.0), 50)
    pp(a)