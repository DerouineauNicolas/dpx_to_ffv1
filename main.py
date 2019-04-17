#!/usr/bin/env python3
import sys, os, fnmatch,  getopt
import fileutils


def usage():
    print("%s is a simple program to convert a set of dpx to ffv1 codec" % sys.argv[0])
    print("Expected usage:")
    print("%s --input=./test/ --output=ffv1out.mkv "% sys.argv[0])

def print_error(error_message):
    print(error_message)
    usage()
    sys.exit()

def parse_directory(path):
    num_scan = None
    offset = None
    name = None
    metadata = {}
    metadata[path] = {}
    meta = metadata[path]
    for files in os.listdir(path):  
        if fnmatch.fnmatch(files, "*.dpx"):
            print(files)
            # Ignore files that don't contains index
            try:
                name, index = fileutils.parse_name(files)
                print(name)
                print(index)
                # This is the first file for that sequence, initialize metadata
                # dictionary with default values and perform a file based probe.
                if name not in meta:
                    #probe = probe_mediainfo(fullpath)['Probe']
                    #probe.pop('CompleteName', None)

                    meta[name] = {
                        #'Folder': dirpath,
                        #'Extension': ext,
                        'Count': 1,
                        'StartIndex': 0,
                        'EndIndex': 0,
                        #'Probe': probe
                    }
                    # Already know this sequence, simply accumulating files
                else:
                    meta[name]['Count'] += 1
                    meta[name]['StartIndex'] = min(index, meta[name]['StartIndex'])
                    meta[name]['EndIndex'] = max(index, meta[name]['EndIndex'])
            except ValueError:
                continue

    return meta[name]['Count'], meta[name]['StartIndex']

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hop:v", ["help", "output=", "input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print_error(err)  # will print something like "option -a not recognized"
    output = None
    input = None
    verbose = False
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
    
    num_scan, offset = parse_directory(input)
    print(num_scan)
    print(offset)
    #encode_dpx_scans(path, output, num_scan, offset, fps)

if __name__ == "__main__":
    main()
