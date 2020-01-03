# PATH

PATH is a folder with all python source codes for modifying Json files.

## JSON FILES DESCRIPTION

node.json : list of nodes with an x, y coordinates and a list of links (routes) with adjacent nodes

dest.json : correspondence between destinations and nodes

## PYTHON FILES DESCRIPTION

add_node.py : script to add a node to node.json 

delete_node.py : script to delete a node from node.json 

display_node.py : script to see the list of nodes 

add_dest.py : script to add a destination to dest.json 

delete_dest.py : script to delete a destination from dest.json 

display_dest.py : script to see the list of destinations

main.py : function to display the shortest path between a source and a destination on the map.png image

## USAGE

add_node.py :

```
python add_node.py id x y [link1 link2 ...]
```

delete_node.py :

```
python delete_node.py id
```

display_node.py : 

```
python display_node.py
```

add_dest.py : 

```
python add_dest.py name node1 [node2 node3 ...]
```

delete_dest.py : 

```
python delete_dest.py name
```

display_dest.py : 

```
python display_dest.py
```

main.py : 

```
python main.py source destination
```
