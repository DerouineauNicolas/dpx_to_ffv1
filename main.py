#!/usr/bin/env python3
import sys, os, fnmatch,  getopt


def usage(prog):
    print("%s is a simple program to convert a set of dpx to ffv1 codec" % prog)
    print("Expected usage:")
    print("%s path=/home/user/dpxdirectory/ output=/home/user/ffv1out.mkv"% prog)

def parse_directory(path):
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            print(entry)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hop:v", ["help", "output=", "input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    input = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage(sys.argv[0])
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            print("output is %s " % output)
        elif o in ("-i", "--input"):
            input = a
            print("path is %s " % path)
        else:
            assert False, "unhandled option"
    
    if input is None:
        print("No input was given")
        usage(sys.argv[0])
        sys.exit()
    if output is None:
        print("No Output was given")
        usage(sys.argv[0])
        sys.exit()
    
    num_scan, offset = parse_directory()
    #encode_dpx_scans(path, output, num_scan, offset, fps)

if __name__ == "__main__":
    main()
