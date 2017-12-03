var request = require('request');

var data = {
    username: "alice",
    password: "h4x00r"
};

var do_request = function(){
    request.get({url: "http://https-only.seclab.space/", timeout: 2000}, function (err, response, body) {
        if (err) return console.log(err);
        var protocol = response.request.uri.protocol;
        request.post(protocol + "//https-only.seclab.space/", {form: data, timeout: 2000}, function (err, response, body) {
            if (err) return console.log(err);
            return console.log("[" + protocol.slice(0, -1) + "] " + response.body);
        });
    });
};

setInterval(do_request, 1 * 3000);