#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests
import sys
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(
        description=
        'extract and download the example inputs for an AtCoder problem.')
    parser.add_argument(
        'url', metavar='url', help='the URL of a AtCoder problem page')
    args = parser.parse_args()

    soup = BeautifulSoup(requests.get(args.url).text, "html.parser")

    parts = soup.find('div', {
        'class': 'io-style'
    }).find_next_siblings('div', {'class': 'part'})

    results = [part.find('pre').text for part in parts]
    for i, result in enumerate(results):
        with open(
                '{}-{}.txt'.format("input" if i % 2 == 0 else "output",
                                   i // 2 + 1), 'w') as f:
            f.write(result)


if __name__ == '__main__':
    main()
