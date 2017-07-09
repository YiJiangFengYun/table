/**
 * Created by YiJiangFengYun on 2017/7/6.
 * entry js
 */
let documentVersion = require("./protobuffCreator/documentVersion");
let Document = require("./protobuffCreator/document");
let Import = require("./protobuffCreator/import");
let Enum = require("./protobuffCreator/types/enum");
let Message = require("./protobuffCreator/types/message");

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
    },
    /**
     * @param {String} name
     * @param {Object?} option
     * @return {Enum}
     */
    createEnum: function (name, option) {
        var e = new Enum(name, option);
        return e;
    },
    /**
     * @param {String} name
     * @param {Object?} option
     * @return {Message}
     */
    createMessage: function (name, option) {
        var msg = new Message(name, option);
        return msg;
    }
};

// module.exports = {};
// module.exports.docVersion = documentVersion;
// module.exports.createDoc = function (name, version, packageName, option) {
//     return new Document(name, version, packageName, option);
// };