
codeTypeMap = {
    js: 0
};

var exportCode = function (doc) {
    for (var key in codeTypeMap) {
        doc.toText();
    }
};

module.exports = {
    codeTypeMap: codeTypeMap,
    exportCode: exportCode
};