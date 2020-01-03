// includes
let express = require("express")
let {execFileSync} = require("child_process")
let fs = require("fs")

let app = express()

// moteur de template
app.set("view engine", "ejs")
app.use(express.static("public"))

//========== Functions ==========//

//========== Routes ==========//

app.get("/", (request, response) =>
{
    let source = request.query.source
    let dest = request.query.dest

    let json_node = JSON.parse(fs.readFileSync("path/node.json"))
    let json_dest = JSON.parse(fs.readFileSync("path/dest.json"))

    if(source === undefined || json_node[source] === undefined)
    {
        response.render("error")
        return
    }

    if(dest !== undefined && json_dest[dest] === undefined)
    {
        response.render("error")
        return
    }

    if(fs.existsSync("public/source_" + source + ".png") === false)
    {
        execFileSync("./display_source.py", [source]).toString()
    }

    let dest_list = []

    for(let d in json_dest)
    {
        dest_list.push(d)
    }
    dest_list.sort()

    if(dest === undefined)
    {
        response.render("home", {source : source, dests : dest_list})
    }
    else
    {
        execFileSync("./path.py", [source, dest])
        response.render("path", {source : source, dest : dest, dests : dest_list})
    }
})

app.listen(8080)
