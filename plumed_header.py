#!/usr/bin/env python3
"""Parse and create headers of plumed data files"""


class PlumedHeader:
    """
    Stores plumed style header in list
    Can parse and create similar headers for usage in python tools

    :param data: list of strings containing the header lines
    :type data: list
    :param delim: comment delimiter to set for the comment lines when printing to file
    :type delim: str
    """

    def __init__(self, header=None, delim="#! "):
        """Instantiate header

        :param header: initial lines of the header without the comment delimiter
        :type header: str or list, optional
        :param delim: comment delimiter to use, defaults to '#! '
        :type delim: str, optional
        """

        self.data = []
        self.delim = delim
        self.set(header)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, line):
        self.replace_line(index, line)

    def __delitem__(self, index):
        del self.data[index]

    def __repr__(self):
        """
        Returns header as string with newlines to be printed to file
        Can be used directly as header argument to numpys savetxt
        """
        return "\n".join([self.delim + line for line in self.data])

    def parse_file(self, filename):
        """
        Saves header of a plumed file to the data list
        The header is assumed to be the first lines of the file that start with the set delimiter
        """
        header = []
        with open(filename) as f:
            for line in f:
                if line.startswith(self.delim):
                    header.append(line.lstrip(self.delim).rstrip("\n"))
                else:
                    self.data = header
                    return

    def add_line(self, line, pos=-1):
        """
        Insert header line at given position (line number starting with 0)
        Defaults to -1 (append)
        This will prepend #! at the start of the line automatically
        """
        if pos == -1:
            self.data.append(line)
        else:
            self.data.insert(pos, line)

    def append_lines(self, lines):
        """
        Append one or multiple lines to header
        """
        if isinstance(lines, list):
            self.data.extend(lines)
        else:
            self.data.append(lines)

    def del_lines(self, pos):
        """
        Delete header lines at given positions
        Requires a list of integers.
        Line numbers are starting with 0
        """
        for i in sorted(pos, reverse=True):
            del self.data[i]

    def replace_line(self, pos, line):
        """
        Replace line at given position
        Line numbers are starting with 0
        """
        del self[pos]
        self.add_line(line, pos)

    def set(self, header):
        """
        Set header to given list of strings
        Will overwrite existing header
        """
        if header is None:
            header = []
        for line in header:
            self.add_line(line)

    def search_lines(self, string):
        """
        Get all lines containing string
        Returns list of tuples (linenumber, line)
        """
        return [(i, line) for i, line in enumerate(self.data) if string in line]
