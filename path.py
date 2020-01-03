#!/usr/bin/env python3

from PIL import Image, ImageDraw
import os
import sys
import json
import math

##### Function #####

def distance(n1, n2):
	return math.sqrt((n1["x"] - n2["x"]) ** 2 + (n1["y"] - n2["y"]) ** 2)

def draw_circle(d, n, r, f):
	d.ellipse((n["x"] - r, n["y"] - r, n["x"] + r, n["y"] + r), fill = f)

def draw_line(d, n1, n2, w):
	d.line([n1["x"], n1["y"], n2["x"], n2["y"]], fill = "blue", width = w)

##### Main #####

if(len(sys.argv) != 3):
    print("Argument error : ./main.py source_id dest")
    exit()

with open('path/node.json') as json_data:
	data = json.load(json_data)

source_id = sys.argv[1]
if source_id not in data:
    print("Argument error : source_id unknown")
    exit()

with open('path/dest.json') as json_data:
    dest = json.load(json_data)

if sys.argv[2] not in dest:
    print("Argument error : dest unknown")
    exit()

dest = dest[sys.argv[2]]

##### Dijkstra #####

for id, node in data.items(): # init

	if id == source_id: # if the node is the source
		node["done"] = True
		node["path"] = [source_id]
		node["length"] = 0
	else:
		node["done"] = False
		if id in data[source_id]["links"]: # if the node is linked to the source
			node["length"] = distance(node, data[source_id])
			node["path"] = [source_id]
		else:
			node["length"] = float("inf")


while(True):

	node_left = []
	for id, node in data.items(): # get all unreached nodes
		if node["done"] == False:
			node_left.append(id)

	if(len(node_left) == 0):
		break

	node_min = node_left[0]

	for id in node_left: # looking for the closest node
		if(data[node_min]["length"] > data[id]["length"]):
			node_min = id

	data[node_min]["done"] = True
	data[node_min]["path"].append(node_min)

	for id in data[node_min]["links"]: # update other nodes
		if data[id]["done"] == False:
			if data[id]["length"] > data[node_min]["length"] + distance(data[id], data[node_min]):
				data[id]["length"] = data[node_min]["length"] + distance(data[id], data[node_min])
				data[id]["path"] = data[node_min]["path"][:]

##### Draw #####

image = Image.open("path/map.png")
draw = ImageDraw.Draw(image)

for id in dest:
	path = data[id]["path"]
	for i in range(1, len(path)):
		draw_line(draw, data[path[i - 1]], data[path[i]], 10)

draw_circle(draw, data[source_id], 25, "red")

for id in dest:
	x = data[id]["x"]
	y = data[id]["y"]
	draw.polygon([x, y, x - 40, y - 80, x + 40, y - 80], fill = "red")

if(os.path.isdir("public/") == False):
	os.mkdir("public/")

image.save("public/path_" + sys.argv[1] + "_" + sys.argv[2] + ".png")
