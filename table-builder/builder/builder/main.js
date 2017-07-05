'use strict';
var path = require("path");
var fsExtra = require("fs-extra");
var traverseFiles = require("./traverse-files");
var edge = require("edge");

var builder = {};
module.exports = builder;

const ENV_DEVELOPMENT = "development";
const ENV_PRODUCTION = "production";

builder.init = function (cb) {
    builder._initConfig(function (err) {
        if (err) {
            cb(err);
            return;
        }
        builder._initEnv(function (err) {
            if (err) {
                cb(err);
                return;
            }

            cb();
        });
    });
}

builder.registerExstension = function (extension) {

}

//start build
//option
//    tableDir
//    isRecursive
builder.build = function (option, cb) {
    builder._buildProto(function (err) {
        if (err) {
            cb(err);
            return;
        }

        builder._parseTables(option, function (err) {
            if (err) {
                cb(err);
                return;
            }

            builder._check(function (err) {
                if (err) {
                    cb(err);
                    return;
                }

                builder._generateBin(function (err) {
                    if (err) {
                        cb(err);
                        return;
                    }

                    cb();
                });

            });
        });
    });
    
}

//Initialize configure setting.
builder._initConfig = function (cb) {
    //Sett builder environment. it can be set to "development" or "production"
    //builder.env = ENV_PRODUCTION;
    builder.env = ENV_DEVELOPMENT;
    cb();
}


//Initialize environment. example: it will install excel-load dll from excel-load project.
builder._initEnv = function (cb) {
    var modulePath = __dirname.substr();
    //copy useful dll from excel-build-cs project.
    console.log("Start copy excel-load dll to dlls");
    var dllDir = builder.env == ENV_DEVELOPMENT ? "./../excel-load/bin/Debug" : "./../excel-load/bin/Release"
    var sourceDir = path.join(modulePath, dllDir);
    var targetDir = path.join(modulePath, "./dlls");
    var excelBuildDllFileName = "excel-load.dll";

    fsExtra.ensureDir(targetDir, err => {
        if (err) {
            cb(err);
            return;
        }
        var copySrcPath = path.join(sourceDir, excelBuildDllFileName);
        var copyTargetPath = path.join(targetDir, excelBuildDllFileName);
        fsExtra.copy(copySrcPath, copyTargetPath, { overwrite: true }, function (err) {
            if (err) {
                return cb(err);
            }
            console.log("Copied " + copySrcPath + " to " + copyTargetPath);
            console.log("Complete copy excel-build-cs dll to dlls");
            cb();
        });
    });
}

//build dynamic proto file, run protoc application to generate proto code for difference languages.
builder._buildProto = function (cb) {
    cb();
}

//load excel table files in specific location, parse they to data arrays.
//then create table objects with these data arrays and proto.
//option:
//    tableDir
//    isRecursive
builder._parseTables = function (option, cb) {
    var tableDir = option.tableDir;
    if (!tableDir) {
        cb("Please specify the table directory for searching tables.");
        return;
    }
    
    traverseFiles(tableDir, function (filePath, fileContent, fileSize, doneCb) {
        var excelFileExt = ".xlsx";
        if (filePath.length > excelFileExt.length &&
            filePath.substr(filePath.length - excelFileExt.length, excelFileExt.length) == excelFileExt) {

            var modulePath = __dirname.substr();
            var assemblyFile = path.join(modulePath, "./dlls/excel-load.dll");
            var buildFromEdge = edge.func({
                assemblyFile: assemblyFile,
                typeName: "excel_load.NodeJsConnector",
                methodName: "Excecute"
            });

            buildFromEdge({
                excelPath: filePath
            }, function (err, result) {
                console.log("complete excel build.");
                doneCb(err);
            });
        }
        else {
            doneCb();
        }
    }, function (err) {
        cb(err);
    });
}

//table js objects check
builder._check = function (option, cb) {
    cb();
}

builder._generateBin = function (cb) {
    cb();
}

