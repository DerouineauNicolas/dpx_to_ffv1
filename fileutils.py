import re

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
