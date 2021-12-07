"""
    generate all possible anagrams of a string (in French)
"""
from argparse import  ArgumentParser
from fulllog import Full_log
import json
import logging
from pathlib import Path
import pickle
import sys

OPTDICTFILE = "../resources/optdict.pkl"
TEXTDICTFILE = "../resources/liste_francais.txt"

def load_textdict(fn):
    """
    :param fn: this is a text file containing most (if not all) words of French language (included their inflected forms) one per line
    :return a dict: which is an optimized access structure to the list of anagrams from their formula
    This remains specific to French, as the file contains French words only.
    Might be changed to other languages.
    """
    try:
        logging.info("Reading dictionary text file")
        with open(fn, "rt", encoding="utf-8") as f:
            s = f.read()
    except OSError as e:
        logging.error(f"Cannot open/read dictionnary text file: {fn}")
        logging.error(f"Reason: {e}")
        logging.error("Exiting now")
        sys.exit(1)
    d = {}
    for w in set(s.split("\n")):
        fw = formula(w)
        d[fw] = d.get(fw, set()) | {w}

    return d


def write_opt_dict(d,fn):
    """ write the optimized dict where the keys are the formulas and the values are the
        list of the anagrams having this very same formula
        :param d dict: the optimize dict structure
        :param fn str: the file path to store the opt dict
        :return None:
    """
    try:
        logging.info("Building optimized dict binary file")
        with open (fn, "wb") as f:
            pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    except OSError as e:
        logging.error(f"Cannot open/write optimized dictionary binary file: {fn}")
        logging.error(f"Reason: {e}")
        logging.error("Exiting now")
        sys.exit(1)


def read_opt_dict(fn):
    try:
        logging.info("Reading optimized dictionnary from binary file")
        with open (fn, "rb") as f:
            return pickle.load(f)
    except OSError as e:
        logging.error(f"Cannot open/read optimized dictionary binary file: {fn}")
        logging.error(f"Reason: {e}")
        logging.error("Exiting now")
        sys.exit(1)


def formula(m):
    """ transforms 'papa' into 'a2p2' """
    d = {c:m.count(c) for c in m}
    return "".join(map(lambda x: x + str(d[x]), sorted(d)))


def main():
    Full_log("anagram")
    logging.info("Anagram started")
    #
    # Prepare argument parser
    #
    ap = ArgumentParser(description="Find the anagrams for a specific string of letters (French)")
    ap.add_argument("-b", "--build",
                    help="build the dict from the available text file",
                    action="store_true")
    ap.add_argument("word",
                    help="the starting point for the anagrams",
                    type=str,
                    nargs='?',
                    default="toupie")
    #
    # Parse args in command line
    #
    args = ap.parse_args()
    #
    # if build is requested or if optimised dict file is missing, then build optimised dict
    #
    if args.build or not Path(OPTDICTFILE).is_file():
        d = load_textdict(TEXTDICTFILE)
        write_opt_dict(d, OPTDICTFILE)
    #
    # Opt dict should be ready
    #
    d = read_opt_dict(OPTDICTFILE)
    try:
        logging.info(f"Searching anagrams for {args.word}")
        print(json.dumps(list(d.get(formula(args.word)))))
    except:
        print(json.dumps(list()))
    logging.info("Anagram completed")

if __name__ == '__main__':
    main()