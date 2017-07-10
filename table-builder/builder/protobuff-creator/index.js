/**
 * Created by YiJiangFengYun on 2017/7/6.
 * entry js
 */
let documentVersion = require("./protobuffCreator/documentVersion");
let buildInTypeMap = require("./protobuffCreator/types/buildInTypes");
let Document = require("./protobuffCreator/document");
let Import = require("./protobuffCreator/import");
let Enum = require("./protobuffCreator/types/enum");
let Message = require("./protobuffCreator/types/message");

module.exports = {
    /**
     * @type {{VERSION_2:number, VERSION_3:number}}
     */
    docVersion: documentVersion,
    buildInTypeMap : buildInTypeMap,
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
    }
};

// module.exports = {};
// module.exports.docVersion = documentVersion;
// module.exports.createDoc = function (name, version, packageName, option) {
//     return new Document(name, version, packageName, option);
// };