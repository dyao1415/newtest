
from urllib import request
import urllib

def is_Important(link: str) -> bool:

    f = urllib.request.urlopen(link)
    opened_file = f.read()
    if "keyword" in opened_file.decode('utf-8'):
        return True
    else:
        return False


with open("urls") as f:
    myline = f.readline()
    while myline:
        print(is_Important(myline))
        myline = f.readline()

