/**
 * Created by YiJiangFengYun on 2017/7/6.
 * entry js
 */
let documentVersion = require("./protobuffCreator/documentVersion");
let Document = require("./protobuffCreator/document");

/**
 *
 * @type {{docVersion: {VERSION_2:number, VERSION_3:number}, createDoc: function(string, number, string, object?):Document}}
 */
module.exports = {
    docVersion: documentVersion,
    createDoc: function (name, version, packageName, option) {
        return new Document(name, version, packageName, option);
    }
};

// module.exports = {};
// module.exports.docVersion = documentVersion;
// module.exports.createDoc = function (name, version, packageName, option) {
//     return new Document(name, version, packageName, option);
// };