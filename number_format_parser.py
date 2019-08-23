#!/usr/bin/env python3
"""
Get number format of a string
"""

def number_format_parse(number):
    # all variables here, could be turned into module
    fmt_char = 'f'
    is_negative = False
    int_length = 0
    dec_length = 0

    try:
        float(number)
    except ValueError:
        print('String is not a number')

    if number[0] == '-':
        is_negative = True

    dot_position = number.find('.')
    if dot_position == -1:
        fmt_str = "%{}.0f".format(len(number) - is_negative)
        return fmt_str

    int_length = dot_position - is_negative

    # check if exponential if dot was in 2nd (with minus 3rd) character
    if dot_position - is_negative == 1:
        for e in ['e', 'E']:
            e_position = number.find(e)
            if e_position != -1:
                fmt_char = e
                dec_length = e_position - dot_position - 1
                break

    if fmt_char == 'f':
        dec_length = len(number) - dot_position - 1

    fmt_str = "%{}.{}{}".format(int_length, dec_length, fmt_char)
    return fmt_str


if __name__ == '__main__':
    numbers = ['21.5624', '1.6345e-5', '6.276E2', '3122225', '-2.43123', '-5.781234e10', '-63214']
    for num in numbers:
        fmt_str = number_format_parse(num)
        formatted_num = fmt_str % (float(num))
        print("{}: {} -> {}".format(num, fmt_str, formatted_num))
