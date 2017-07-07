'use strict';
let builder = require("./../builder");

builder.init(function (err) {
    if (err) {
        console.log(err);
        return;
    }
    //builder.registerExstension();
    builder.build(
        {
            tableDir: "table-example-excel"
        }, function (err) {
            if (err) {
                console.log(err);
                return;
            }

            console.log("table build complete!");
        });
});

