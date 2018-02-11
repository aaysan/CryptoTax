var express     = require("express");
var app         = express();
var bodyparser  = require("body-parser");
var window = require("window");
var open = require('open');    
// var exec        = require('child_process').execFile;
const exec = require("child_process").exec;

app.use(bodyparser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");

app.get("/convert", function(req, res) {
    var user = {
        username: "rpatni"
    }
    res.locals.currentUser = user;
    res.render("convert");

    // var fun =function(){
    // console.log("fun() start");
    // exec("../dist/index", function(err, data) {  
    //         console.log(err)
    //         console.log(data.toString());                       
    //     });  
    // }
    // fun();

    exec("./dist/index", (error, stdout, stderr) => {
        if (error) {
            console.log(error);
        }
        
            console.log(stdout);
        
    });

    //require("openurl").open("/file1")
    setTimeout(delay,2000);

    
    
    // window.open("https://drive.google.com/open?id=1REgq0sHejx0VG8LdCnv5l2lN17U7cX7a", "_blank");
});

function delay(){
    open("https://drive.google.com/open?id=1REgq0sHejx0VG8LdCnv5l2lN17U7cX7a");
};

app.get("/login", function(req, res) {
    res.render("login")
});

app.get("/file1", function(req, res) {
    res.render("form1");
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