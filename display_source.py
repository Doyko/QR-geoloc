#!/usr/bin/env python3

from PIL import Image, ImageDraw
import os
import json
import sys

if(len(sys.argv) != 2):
    print("Argument error : ./display_source.py id")
    exit()

id = sys.argv[1]

with open("path/node.json") as json_data:
    node = json.load(json_data)

if id not in node:
    print("Argument error : id unknown")
    exit()

# display on picture

def draw_circle(d, n, r, f):
	d.ellipse((n["x"] - r, n["y"] - r, n["x"] + r, n["y"] + r), fill = f)

image = Image.open("path/map.png")
draw = ImageDraw.Draw(image)

draw_circle(draw, node[id], 25, "red")

if(os.path.isdir("public/") == False):
	os.mkdir("public/")

image.save("public/source_" + id + ".png")
