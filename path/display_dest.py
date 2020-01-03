#!/usr/bin/env python3

import json

with open("dest.json") as json_dest:
    dest = json.load(json_dest)

for name, nodes in dest.items():
    print(name + " : " + str(nodes))
