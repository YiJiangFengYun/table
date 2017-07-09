/**
 * Created by YiJiangFengYun on 2017/7/6.
 * entry js
 */
let documentVersion = require("./protobuffCreator/documentVersion");
let Document = require("./protobuffCreator/document");
let Import = require("./protobuffCreator/import");

module.exports = {
    /**
     * @type {{VERSION_2:number, VERSION_3:number}}
     */
    docVersion: documentVersion,
    /**
     * @param {String} name
     * @param {Number} version
     * @param {String} packageName
     * @param {Object?} option
     * @return {Document}
     */
    createDoc: function (name, version, packageName, option) {
        var doc = new Document(name, version, packageName, option);
        return doc;
    },
    /**
     * @param {String} name
     * @param {Object?} option
     * @return {Import}
     */
    createImport: function (name, option) {
        var imp = new Import(name, option);
        return imp;
    }
};

// module.exports = {};
// module.exports.docVersion = documentVersion;
// module.exports.createDoc = function (name, version, packageName, option) {
//     return new Document(name, version, packageName, option);
// };