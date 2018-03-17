import os

__author__ = 'KaiZhou'

suffix = ('.txt',
        '.ilk',
        '.pdb',
        '.iobj',
        '.ipdb',
        '.exe',
        '.user',
        '.log',
        '.pch',
        '.tlog',
        '.db',
        '.opendb',
        '.ipch',
        '.suo',
        '.obj',
        '.lastbuildstate',
        '.idb',
        '')

def _getDirs(path='.'):
    dirs =[os.path.join(path,x) for x in os.listdir(path)]
    return dirs

def _containExt(ext):
    for i in suffix:
        if i == ext:
            return True
    return False

def _RemoveTemporaryFile(path='.'):
    dirs = _getDirs(path)
    for i in dirs:
        if os.path.isdir(i):
            _RemoveTemporaryFile(i)
        else:
           if _containExt(os.path.splitext(i)[1]):
                os.remove(i)
                print("start remove file:%s" % i)

def _RemoveEmptyDirectory(path='.'):
    dirs = _getDirs(path)
    for i in dirs:
        if os.path.isdir(i):
            if len(os.listdir(i)) == 0:
                os.removedirs(i)
                print('start remove directory:%s'% i)
            else:
                _RemoveEmptyDirectory(i)

def CleanBuildTree(path='.'):
    _RemoveTemporaryFile(path)
    _RemoveEmptyDirectory(path)


if __name__=='__main__':
    CleanBuildTree()
