#!/usr/bin/env python3

import sys
import json

filename = "dest.json"

if(len(sys.argv) != 2):
    print("Argument error : ./delete_dest.py name")
    exit()

name = sys.argv[1]

with open(filename) as json_dest:
    dest = json.load(json_dest)

if name not in dest:
    print("Argument error : name unknown")
    exit()

dest.pop(name, None)

f = open(filename, "w")
json.dump(dest, f)
f.close()
