
# compare contents of two files in binary form
import sys

def compareFile(srcFile,destFile):
    with open(srcFile,"rb") as src:
        srcData = src.read()
    with open(destFile,"rb") as dest:
        destData = dest.read()
    checked = False
    if(len(srcData)!=len(destData)):
        print("It unequal between ",srcFile,destFile,". The file size is different")
        checked = True
    for i in range(min(len(srcData),len(destData))):
        if(srcData[i] != destData[i]):
            print("unequal index:%d, modleDatata:%d, flashData:%d "  % (i,srcData[i],destData[i]))
            checked = True
    if checked:
        print('Check Result: unequal')
    else:
        print('Check Result: equal')

def main():
    if(len(sys.argv) !=3 ):
        print('Wrong parameters,need two files')
        return
    compareFile(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()