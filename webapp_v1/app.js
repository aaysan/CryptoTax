var express     = require("express");
var app         = express();
var bodyparser  = require("body-parser");

app.use(bodyparser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");

router.get("/", function(req, res) {
    res.redirect("landing");
});

router.get("*", function(req, res) {
    res.redirect("/");
});

app.listen(3000, function(req, res) {
    console.log("Started YelpCamp V1 Server");
});