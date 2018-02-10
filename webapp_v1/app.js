var express     = require("express");
var app         = express();
var bodyparser  = require("body-parser");

app.use(bodyparser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");

app.get("/convert", function(req, res) {
    var user = {
        username: "rpatni"
    }
    res.locals.currentUser = user;
    res.render("convert");
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