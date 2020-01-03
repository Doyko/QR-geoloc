#!/usr/bin/env python3

import sys
import json

filename = "dest.json"

if(len(sys.argv) < 3):
    print("Argument error : ./add_dest.py name node1 [node2 node3 ...]")
    exit()

with open(filename) as json_dest:
    dest = json.load(json_dest)

with open("node.json") as json_node:
    nodes = json.load(json_node)

name = sys.argv[1]
nodes_list = sys.argv[2:]

if name in dest:
    print("Argument error : name already exists")
    exit()

for n in nodes_list:
    if n not in nodes:
        print("Argument error : node {} doesn't exist".format(n))
        exit()

dest[name] = nodes_list

f = open(filename, "w")
json.dump(dest, f)
f.close()
