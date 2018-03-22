
# compare contents of two files in binary form
import sys

modelPath="model.bin"
flashPath="flash.bin"
def compareFile(srcFile,destFile):
    try:
        src = open(srcFile,"rb")
    except OSError as e:
        print("except:",e)
        return
    srcData = src.read()
    src.close()
    try:
        dest = open(destFile,"rb")
    except OSError as e:
        print('except:',e)
        return 
    destData = dest.read()
    dest.close()
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