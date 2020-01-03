#!/usr/bin/env python3

from PIL import Image, ImageDraw
import json

with open("node.json") as json_data:
    data = json.load(json_data)

# print in terminal

for id, node in data.items():
    print(id + " : coord [ " + str(node["x"]) + ", " + str(node["y"]) + "] links : " + str(node["links"]))

# display on picture

def draw_circle(d, n, r):
	d.ellipse((n["x"] - r, n["y"] - r, n["x"] + r, n["y"] + r), fill = "red")

def draw_line(d, n1, n2, w):
	d.line([n1["x"], n1["y"], n2["x"], n2["y"]], fill = "blue", width = w)

image = Image.open("map.png")
draw = ImageDraw.Draw(image)

for id, node in data.items():
	for link in node["links"]:
		draw_line(draw, node, data[link], 10)

for id, node in data.items():
	draw_circle(draw, node, 25)

image.save("all_nodes.png")
