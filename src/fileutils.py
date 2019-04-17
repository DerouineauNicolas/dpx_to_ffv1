import re, os, fnmatch


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
                name, index = parse_name(files)
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
                        'StartIndex': index,
                        'EndIndex': 0,
                        #'Probe': probe
                    }
                    # Already know this sequence, simply accumulating files
                else:
                    meta[name]['Count'] += 1
                    meta[name]['StartIndex'] = min(
                        index, meta[name]['StartIndex'])
                    meta[name]['EndIndex'] = max(index, meta[name]['EndIndex'])
            except ValueError:
                continue

    return meta[name]['Count'], meta[name]['StartIndex']


IMAGENO_REGEX = re.compile(r'[\._]?(?P<Index>\d+)(?=[\._])')


def parse_name(filename, regex=IMAGENO_REGEX):
    """ Extract image name and index from filename.

        Args:
            filename (str): Image file name.
            regex (RegexObject): Extraction rule.

        Returns:
            Tuple (name, index) extracted from filename.

        Raises:
            ValueError: If image index not found in ``filename``.

        >>> parse_name('myfile.0001.tiff')
        ('myfile', 1)
        >>> parse_name('myfile_0001.tiff')
        ('myfile', 1)
        >>> parse_name('myfile.123.0001.tiff')
        ('myfile.123', 1)
        >>> parse_name('00123060.tiff')
        ('', 123060)
        >>> parse_name('123060.tiff')
        ('', 123060)
        >>> parse_name('myfile.tiff')
        Traceback (most recent call last):
        ...
        ValueError: myfile.tiff : image index not found
        >>> parse_name('myfile.abcdef.tiff')
        Traceback (most recent call last):
        ...
        ValueError: myfile.abcdef.tiff : image index not found

    """
    m = list(regex.finditer(filename))
    if m == []:
        raise ValueError('{} : image index not found'.format(filename))

    lastm = m[-1]
    name = filename[:lastm.start()]
    index = lastm.groupdict()['Index']
    return name, int(index)
