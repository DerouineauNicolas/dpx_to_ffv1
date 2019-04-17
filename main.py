#!/usr/bin/env python3
import sys, os, fnmatch,  getopt


def usage():
    print("coucou")

def encode_dpx_scans(path, output, fps=24):
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:p:o", ["help", "path=", "output="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
            print("path is %s"%path)
        elif opt in ("-o", "--output"):
            output = arg

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[])