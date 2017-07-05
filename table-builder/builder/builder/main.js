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
    builder._buildCommonProto(function (err) {
        if (err) {
            cb(err);
            return;
        }

        builder._parseTables(option, function (tablesOfTable, cb) {
            builder._buildTable(tablesOfTable, function (err) {
                if (err) {
                    cb(err);
                    return;
                }

                cb();
            });
        }, function (err) {
            if (err) {
                cb(err);
                return;
            }

            //complete build tables work
            cb();
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

//build common dynamic proto file, run protoc application to generate proto code for difference languages.
builder._buildCommonProto = function (cb) {
    cb();
}

//load excel table files in specific location, parse they to data arrays.
//option:
//    tableDir
//    isRecursive
builder._parseTables = function (option, eachCb, cb) {
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
                if (err) {
                    doneCb(err);
                    return;
                }

                if (result.isComplete == false) {
                    doneCb(result.msg);
                    return;
                }

                eachCb(result.tables, function (err) {
                    doneCb(err);
                });
            });
        }
        else {
            doneCb();
        }
    }, function (err) {
        cb(err);
    });
}


builder._buildTable = function (tablesOfTable, cb) {
    builder._buildTableProto(tablesOfTable, function (err) {
        if (err) {
            cb(err);
            return;
        }

        builder._createTableObjs(tablesOfTable, function (err) {
            if (err) {
                cb(err);
                return;
            }

            builder._checkTable(function (err) {
                if (err) {
                    cb(err);
                    return;
                }

                builder._generateTableBin(function (err) {
                    cb(err);
                });
            });

        })
    })
}

//build table dynamic proto file, run protoc application to generate proto code for difference languages.
builder._buildTableProto = function (tablesOfTable, cb) {
    cb();
}

//generate table js objects
builder._createTableObjs = function (tablesOfTable, cb) {
    cb();
}

//table js objects check
builder._checkTable = function (cb) {
    cb();
}

builder._generateTableBin = function (cb) {
    cb();
}

