#!/usr/bin/env python3
"""Parse and create headers of plumed data files"""


class PlumedHeader:
    """
    Stores plumed style header in list
    Can parse and create similar headers for usage in python tools

    :param fields: list of strings containing the column descriptions
    :type fields: list
    :param constants: dictionary of constants for the data
    :type fields: dict {name: val}
    :param delim: comment delimiter to set for the comment lines when printing to file
    :type delim: str
    """

    def __init__(self, fields=None, constants=None, delim="#!"):
        """Instantiate header

        :param fields: list holding description of the data columns, optional
        :param constants: dictionary with additional constants, optional
        :param delim: comment delimiter to use, defaults to '#!'
        :type delim: str, optional
        """
        self.fields = fields or []
        self.constants = constants or {}
        self.delim = delim

    def __repr__(self):
        """
        Returns header as string with newlines to be printed to file.
        Can be used directly as header argument to numpys savetxt.
        """
        lines = []
        lines.append(self.delim + " FIELDS " + " ".join(self.fields))
        for name, value in self.constants.items():
            lines.append(f"{self.delim} SET {name} {value}")
        return "\n".join(lines)

    def parse_file(self, filename, delim=None):
        """
        Parse header of plumed file.

        The header is assumed to be the first lines of the file that start with the set delimiter.
        This overwrites the existing fields and constants of the class instance.
        If no custom delimiter is specified the one of the class instance is used.

        :param filename: file to parse
        :param delim: comment delimiter of file, optional
        """
        if not delim:
            delim = self.delim

        header = []
        with open(filename, "r") as f:
            for line in f:
                if line.startswith(delim):
                    header.append(line.lstrip(delim).rstrip("\n").strip())
        if not header:
            raise ValueError(f"No header was found in specified file {filename}")

        # first line contains description of columns
        if header[0].startswith("FIELDS"):
            self.fields = header[0].split()[1:]
        else:
            raise ValueError(f"No FIELDS found in specified file {filename}")

        # (optional) remaining lines contain constants
        for line in header[1:]:
            if line.startswith("SET"):
                name, val = line.split()[1:3]
                self.constants[name] = val

    def set_constant(self, name, val):
        """
        Add constant to header. Will overwrite existing value of same name

        :param name: Name of constant
        :param val: Value of constant (will be cast to str)
        """
        self.constants[name] = str(val)

    def add_field(self, name):
        """
        Append field to header

        :param name: name of field
        """
        self.fields.append(name)
