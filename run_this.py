from documents import Documents
from pprint import pprint


TALES_FILE = "AesopTales.txt"

def get_tales(TALES_FILE):
    tales = {};
    with open(TALES_FILE) as file:
        for tale in file.read().split("\n\n"):
            th = 0
            fl = ""
            for line in tale.split("\n"):
                line = line.strip(" ")
                if line != "":
                    if not th:
                        tales[line] = ""
                        fl = line
                        s = fl
                        th=1
                    else:
                        tales[fl] += line.lower()
    return tales


if __name__ == "__main__":
    tales = get_tales(TALES_FILE)
    doc = Documents(tales)

    # Question 1
    pprint(doc.all_in_all("hired"), indent=4)
    print("\n\n\n");print("------------------------------------------");print("\n\n\n")
    #Question 2
    pprint(doc.one_in_all("hired"), indent=4)
    print("\n\n\n");print("------------------------------------------");print("\n\n\n")
    #Question 3
    pprint({"relavance":doc.relevence("hired")}, indent=4)
    print("\n\n\n");print("------------------------------------------");print("\n\n\n")
