#!/usr/bin/env python3
import sys, os, fnmatch,  getopt
from dpx2ffv1.fileutils import parse_directory 
from dpx2ffv1.encode import is_ffmpeg_available, encode_dpx_scans 

def usage():
    print("dpx2ffv1 is a simple module to convert a set of dpx to ffv1 codec")
    print("Expected usage:")
    print("python3 -m dpx2ffv1 --input=./test/ --output=ffv1out.mkv ")

def print_error(error_message):
    print(error_message)
    usage()
    sys.exit()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hop:v", ["help", "output=", "input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print_error(err)  # will print something like "option -a not recognized"
    output = None
    input = None
    verbose = False
    fps = 24

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            print("output is %s " % output)
        elif o in ("-i", "--input"):
            input = a
            print("path is %s " % input)
            if(os.path.isdir(input) == False):
                print_error("The input path is not a directory")
        else:
            assert False, "unhandled option"
    
    if input is None:
        print_error("No input was given")
    if output is None:
        print_error("No Output was given")
    
    num_scan, offset, num_decimal, prefix = parse_directory(input)

    if(is_ffmpeg_available()==True):
        try:
            ret = encode_dpx_scans(input, output, num_scan, offset, fps, num_decimal, prefix)
            if ret < 0:
                print("Something went wrong")
                sys.exit(-1)
            else:
                print("Encoding is finished")
        except Exception:
            print("Something went wrong")
            sys.exit(-1)
        
    else:
        print_error("ffmpeg is not installed")

if __name__ == "__main__":
    main()
