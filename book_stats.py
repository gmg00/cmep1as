#!/usr/bin/env python
# Copyright (C) 2022 luca.baldini@pi.infn.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23.
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np


def process(file_path, histogram_switch):
    """Get file_path and histogram_switch, if it's True process call build_histogram.
    """
    print(f'Opening input file {file_path}...')
    # Get the text.
    with open(file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    # Get the dictionary with letters and their occurences.
    letters = get_letters(text)
    print(letters)
    # Build histogram.
    if histogram_switch:
        build_histogram(letters)
    print('Done.')

def get_letters(text):
    """ Create a dictionary (letters), put chars as keys and give them as values
    the number of occurences.
    """
    letters = {} # Dictionary.

    for element in text:
        # If the element is not in letters it creates a new key and gives it as value
        # the number of occurences.
        if element not in letters:
            letters[str(element)] = text.count(element)
    # Sort the keys in alphabetic order (upper case letters and lower case letters
    # are different characters).
    letters = dict(sorted(letters.items()))
    return letters

def build_histogram(letters):
    """ Create an histogram with letters on x-axis and the number of occurences on
    y-axis.
    """
    # Get the keys and values from letters dictionary.
    letters_keys = list(letters.keys())
    letters_values = list(letters.values())
    # Get letters from 'A' to 'Z' and their relative occurences.
    x_values = letters_keys[letters_keys.index('A') : letters_keys.index('Z')+1]
    # Add occurences of upper case letters and lower case letters.
    y_values = np.add(letters_values[letters_keys.index('A') : letters_keys.index('Z')+1],
                      letters_values[letters_keys.index('a') : letters_keys.index('z')+1])

    # Build histogram.
    plt.figure(1)
    x_pos = np.arange(len(x_values))
    plt.bar(x_pos, y_values) # Histogram.
    plt.title('Histogram')
    plt.xlabel('Letters')
    plt.ylabel('Occurences')
    plt.xticks(x_pos, x_values) # Write letters on x-axis.
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    parser.add_argument('--histogram', action='store_true')
    args = parser.parse_args()
    process(args.infile, args.histogram)
