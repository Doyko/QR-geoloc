# PRESENTATION OF THE PROJECT

The project is a web application that resolves QR-codes into indoor positions and computes itineraries within buildings.

## USAGE

In order to run the server, you first need to install node.js and npm on your computer.

Install the dependencies :

```
npm install
```

Run the server :

```
node server.js
```

## PROJECT STRUCTURE

### path

`path` is a folder that contain the map (in png format), Json files and all python scripts needed to create these resources.

### public

`public` is a folder with all the generated images showed to the user.

### views

`views` is a folder with all the front end of the web application.

### path.py

path.py : script to generate the image of the path to destination.

### display_source.py

display_source.py : script to generate the image of the source.

### package.json

package.json : list of the module that need to be imported by npm.

### server.js

server.js : the server is used to run the web application.
