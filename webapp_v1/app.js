var express     = require("express");
var app         = express();
var bodyparser  = require("body-parser");
var exec        = require('child_process').execFile;

app.use(bodyparser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");

app.get("/convert", function(req, res) {
    var user = {
        username: "rpatni"
    }
    res.locals.currentUser = user;
    res.render("convert");

    var fun =function(){
    console.log("fun() start");
    exec("../dist/index", function(err, data) {  
            console.log(err)
            console.log(data.toString());                       
        });  
    }
    fun();
});

app.get("/", function(req, res) {
    res.render("landing");
});

app.get("*", function(req, res) {
    res.redirect("/");
});

app.listen(3000, function(req, res) {
    console.log("Started YelpCamp V1 Server");
});