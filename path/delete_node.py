#!/usr/bin/env python3

import sys
import json

if(len(sys.argv) != 2):
    print("Argument error : ./delete_node.py id")
    exit()

id = sys.argv[1]

# delete from node.json

filename = "node.json"

with open(filename) as json_node:
    node = json.load(json_node)

if id not in node:
    print("Argument error : id unknown")
    exit()

for link in node[id]["links"]:
    node[link]["links"].remove(id)

node.pop(id, None)

f = open(filename, "w")
json.dump(node, f)
f.close()

#delete from dest.json

filename = "dest.json"

with open(filename) as json_dest:
    dest = json.load(json_dest)

for d in dest:
    if id in dest[d]:
        dest[d].remove(id)

f = open(filename, "w")
json.dump(node, f)
f.close()
