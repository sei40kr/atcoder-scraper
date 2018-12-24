#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pathlib
import requests
import sys
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(
        description=
        'extract and download the example inputs for an AtCoder problem.')
    parser.add_argument(
        'path', metavar='path', help='the path to your solution')
    parser.add_argument(
        'url', metavar='url', help='the URL of a AtCoder problem page')
    args = parser.parse_args()

    soup = BeautifulSoup(requests.get(args.url).text, "html.parser")

    parts = soup.find('div', {
        'class': 'io-style'
    }).find_next_siblings('div', {'class': 'part'})
    parts = [part for i, part in enumerate(parts) if i % 2 == 0]

    results = [part.find('pre').text for part in parts]
    for i, result in enumerate(results):
        with open('{}.qrinput{}'.format(args.path, i + 1), 'w') as f:
            f.write(result)


if __name__ == '__main__':
    main()
