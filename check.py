import os


def checkDirExists(dir):
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir)
