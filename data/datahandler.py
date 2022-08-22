import pickle
from os import path


class dataholder():
    def __init__(self) -> None:
        self.written = []
        self.pressed = False


dh = dataholder()


def write(file, towrite=dh.written):
    try:
        with open(file, 'rb') as f:
            dh.written = pickle.load(f)
    except:
        dh.written = []
    with open(file, 'wb') as f:
        if towrite != dh.written:
            dh.written.append(towrite)
        pickle.dump(dh.written, f)
    print("Wrote to file")


def replace(file, index, toreplace):
    try:
        with open(file, 'rb') as f:
            dh.written = pickle.load(f)
        dh.written[index] = toreplace
        write(file)
    except Exception as e:
        print(e)


def read(file: str):
    if path.getsize(file) > 0:
        with open(file, 'rb') as f:
            content = pickle.load(f)
            if type(content) is str:
                if len(content.split("\n")) > 1:
                    return content.split("\n")
                else:
                    return content
            else:
                return content
    else:
        return ""


def getdh(): return dh
