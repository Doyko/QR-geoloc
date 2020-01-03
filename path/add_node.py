#!/usr/bin/env python3

import sys
import json

filename = "node.json"

if(len(sys.argv) < 4):
    print("Argument error : ./add_node.py id x y [link1 link2 ...]")
    exit()

with open(filename) as json_data:
    data = json.load(json_data)

id = sys.argv[1]
links = sys.argv[4:]

if id in data:
    print("Argument error : id already exists")
    exit()

data[id] = {}
data[id]["x"] = int(sys.argv[2])
data[id]["y"] = int(sys.argv[3])
data[id]["links"] = links

for link in links:
    if link in data:
        data[link]["links"].append(id)
    else:
        print("Argument error : link doesn't exist")
        exit()

f = open(filename, "w")
json.dump(data, f)
f.close()
