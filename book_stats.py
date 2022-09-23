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


def process(file_path):
    """Get file_path and process stats.
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    letters = get_letters(text)
    print(letters)
    build_histogram(letters)
    print('Done.')

def get_letters(text):
    """Create a dictionary (letters), put chars as keys and give them as values
    the number of occurences.
    """
    letters = {}
    for element in text:
        if not element in letters:
            letters[str(element)] = text.count(element)
    letters = dict(sorted(letters.items()))
    return letters

def build_histogram(letters):
    """
    """
    letters_keys = list(letters.keys()) 
    letters_values = list(letters.values())
    x_values = letters_keys[letters_keys.index('A') : letters_keys.index('Z')]
    y_values = letters_values[letters_keys.index('A') : letters_keys.index('Z')]
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    process(args.infile)