"""
    generate all possible anagrams of a string
"""
import pickle
import sys
import json



# def load_dict1(fn):
#     try:
#         with open(fn, "rt", encoding="utf-8") as f:
#             s = f.read()
#     except FileNotFoundError:
#         print("Cannot open/read file: ", fn)
#         sys.exit(1)
#     return set(s.split("\n"))


def load_dict(fn):
    try:
        with open(fn, "rt", encoding="utf-8") as f:
            s = f.read()
    except FileNotFoundError:
        print("Cannot open/read file: ", fn)
        sys.exit(1)
    d = {}
    for w in set(s.split("\n")):
        fw = formula(w)
        d[fw] = d.get(fw, set()) | {w}

    return d


def write_dict(d):
    with open ("resources/optdict.pkl", "wb") as f:
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)


def read_dict():
    with open ("resources/optdict.pkl", "rb") as f:
        return pickle.load(f)


def formula(m):
    d = {c:m.count(c) for c in m}
    return "".join(map(lambda x: x + str(d[x]), sorted(d)))


# def buildDictionary(m):
#     # d=load_dict("resources/liste.de.mots.francais.frgut.txt")
#     d=load_dict("resources/liste_francais.txt")
#     write_dict(d)

d = read_dict()
m = "toupie" # a default to be used if command line does not content a word to start with
if len(sys.argv)>1:
    m = sys.argv[1]

try:
    print(json.dumps(list(d.get(formula(m)))))
except:
    print(json.dumps(list()))