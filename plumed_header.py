#!/usr/bin/env python3
"""Parse and create headers of plumed data files"""

class PlumedHeader:
    """
    Stores plumed style header in list
    Can parse and create similar headers for usage in python tools
    """

    def __init__(self):
        self.data = []


    def string(self):
        """
        Returns header as string with newlines to be printed to file
        Can be used directly as header argument to numpys savetxt
        """
        return ''.join(self.data)


    def parse_file(self, filename):
        """
        Saves header of a plumed file as list
        Includes the newline characters at the end of every line
        """
        header = []
        for line in open(filename):
            if line.startswith('#!'):
                header.append(line)
            else:
                self.data = header
                return
        raise ValueError("End of file reached. Is this really a plumed data file?")


    def add_line(self, line, pos=-1):
        """
        Insert header line at given position (line number starting with 0)
        Defaults to -1 (append)
        """
        if pos == -1:
            self.data.append(line + '\n')
        else:
            self.data.insert(pos, line + '\n')


    def replace_line(self, line, pos):
        """
        Replace header line at given position (line number starting with 0)
        """
        if pos >= len(self.data) or pos < 0:
            raise ValueError("Trying to replace a nonexistant header line.")
        self.data[pos] = line


    def del_line(self, pos):
        """
        Delete header line at given position (line number starting with 0)
        """
        del self.data[pos]


    def set(self, header):
        """
        Set header to given list of strings
        Will overwrite existing header
        """
        self.data = header


    def get_fields(self):
        """
        Get column titles from the FIELDS line
        """
        return [field[2:] for field in [line.split() for line in self.data] if field[1] == "FIELDS"]


    def search_lines(self, string):
        """
        Get all lines containing string
        Returns list of tuples (linenumber, line)
        """
        return [(i, line) for i, line in enumerate(self.data) if string in line]
