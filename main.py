#!/usr/bin/env python3
import sys, os, fnmatch,  getopt
import src.fileutils as fileutils
import src.encode as encode


def usage():
    print("%s is a simple program to convert a set of dpx to ffv1 codec" % sys.argv[0])
    print("Expected usage:")
    print("%s --input=./test/ --output=ffv1out.mkv "% sys.argv[0])

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
    
    num_scan, offset = fileutils.parse_directory(input)
    print("Num scan = %d" % num_scan)
    print("offset = %d" % offset)
    if(encode.is_ffmpeg_available()==True):
        encode.encode_dpx_scans(input, output, num_scan, offset, fps)
    else:
        print_error("ffmpeg is not installed")

if __name__ == "__main__":
    main()
