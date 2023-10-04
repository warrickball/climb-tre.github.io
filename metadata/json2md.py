#!/usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('json_filename', type=str)
parser.add_argument('--title', type=str)
args = parser.parse_args()

import sys
import json

with open(args.json_filename, 'r') as f:
    j = json.load(f)

required = [
    ['Column name', 'Data type', 'Description'],
    ['-----']*3,
]
optional = [row[:] for row in required]  # deep copy

for k, v in j['data'].items():
    try:
        row = [k, v['type'], v['description']]

        if v['required']:
            required.append(row)
        else:
            optional.append(row)

    except:
        print("WARNING: could not create entry for key %s" % k, file=sys.stderr)

if args.title:
    print('# ' + args.title)
    print()

print('## Required\n')
print(''.join(['| ' + ' | '.join(row) + ' |\n' for row in required]))
print('## Optional\n')
print(''.join(['| ' + ' | '.join(row) + ' |\n' for row in optional]))
