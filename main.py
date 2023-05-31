import requests
from bs4 import BeautifulSoup


def fill_list(txt_file: str) -> list:
    ret = []
    with open(txt_file) as open_File:
        open_File_Line = open_File.readline()
        while open_File_Line:
            ret.append(open_File_Line)
            open_File_Line = open_File.readline()
    return ret


def is_Important(url: str) -> bool:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = soup.get_text()
    if "keyword" in soup2:
        return True
    else:
        return False


testing = fill_list("urls")
for link in testing:
    print(is_Important(link))

print("Testing out if I succesfully linked Git")
