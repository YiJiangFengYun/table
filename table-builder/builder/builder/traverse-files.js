var fs = require("fs");
var path = require("path");
var async = require("async");

/**
 * read all file in specified directory includes sub directorys, return file content (raw buffer)
 * @param {string} dir
 * @param {function(string, Buffer, number, function(Error):void):void} iterator called when traverse each file, gived file path and file content buffer.
 * @param {function(Error):void} doneCb  complete call back
 */
function traverse(dir, iterator,  doneCb) {
    fs.readdir(dir, function (err, list) {
        if (err) return doneCb(err);
        async.each(list, function (file, doneCb) {
            var filePath = path.join(dir, file);
            fs.stat(filePath, function (err, stats) {
                if (err) return doneCb(err);
                if (stats.isDirectory()) {
                    return traverse(filePath, iterator, doneCb);
                }
                else {
                    fs.readFile(filePath, function (err, data) {
                        if (err) return doneCb(err);
                        iterator(filePath, data, stats.size, function (err) {
                            doneCb(err);
                        });
                    });
                }
            });

        }, function (err) {
            doneCb(err, null);
        });
    });
}

module.exports = traverse;