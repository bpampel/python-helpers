#!/usr/bin/env python3
"""
Class to store format of numbers
can also parse strings to determine their format
"""

class NumberFmt:
    def __init__(self):
        self.flag = '-'
        self.specifier = 'f'
        self.width = 12
        self.precision = 6

    def parser(self, number):
        """Parse format of number string"""
        is_signed = False

        try:
            float(number)
        except ValueError:
            print('String is not a number')

        if number[0] == '+':
            is_signed = True
            self.flag ='+'
        elif number[0] == '-':
            is_signed = True
            # can't say anything about the flag then

        dot_position = number.find('.')
        if dot_position == -1: # number is an integer
            self.precision = 0
            self.width = len(number) - is_signed
            return

        self.width = len(number) - is_signed - 1

        # check if exponential if dot was at 2nd position
        if dot_position - is_signed == 1:
            for e in ['e', 'E']:
                e_position = number.find(e)
                if e_position != -1:
                    self.specifier = e
                    self.precision = e_position - dot_position - 1
                    break

        self.precision = len(number) - dot_position - 1
        return


    def get(self):
        """Return format as C style string"""
        fmt_str = "%{}{}.{}{}".format(self.flag, self.width, self.precision, self.specifier)
        return fmt_str


    # def set(self, format_string):



if __name__ == '__main__':
    numbers = ['21.5624', '1.6345e-5', '6.276E2', '3122225', '-2.43123', '-5.781234e10', '-63214']
    for num in numbers:
        fmt = NumberFmt()
        fmt.parser(num)
        formatted_num = fmt.get() % (float(num))
        print("{}: {} -> {}".format(num, fmt.get(), formatted_num))
