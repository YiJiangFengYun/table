/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Document Type
 */
let Base = require("./base");
let Syntax = require("./syntax");
let Package = require("./package");
let docVersion = require("./documentVersion");

/**
 * Proto buff document
 * @param {string} name
 * @param {number} version
 * @param {string} packageName
 * @param {object?} option
 *
 * @class
 * @constructor
 */
let Document = function (name, version, packageName, option) {
    Base.call(this, name, option);
    this.version = version || docVersion.VERSION_3;
    this.syntax = new Syntax("documentSyntax", {version: this.version});
    this.package = new Package(packageName);
    this.imports = [];
    this.enums = [];
    this.messages = [];
};

Document.prototype = Object.create(Base.prototype);
Document.prototype.constructor = Document;

/**
 * @memberOf Document
 */
Document.prototype.dispose = function () {
    this.syntax = null;
    this.package = null;
    this.imports.length = 0;
    this.imports = null;
    this.enums.length = 0;
    this.enums = null;
    this.messages.length = 0;
    this.messages = null;
};

/**
 * create text
 * @return {string}
 *
 * @memberOf Document
 */
Document.prototype.toText = function () {
    let resultStr = "";
    let len;
    let i;

    //syntax
    resultStr += this.syntax.toText();

    //package
    resultStr += this.package.toText();

    //imports
    let imports = this.imports;
    len = imports.length;
    for (i = 0; i < len; ++i) {
        resultStr += imports[i].toText();
    }

    //enums
    let enums = this.enums;
    len = enums.length;
    for (i = 0; i < len; ++i) {
        resultStr += enums[i].toText();
    }

    //messages
    let messages = this.messages;
    len = messages.length;
    for (i = 0; i < len; ++i) {
        resultStr += messages[i].toText();
    }

    return resultStr;

};

/**
 * Add import
 * @param {Import} newImport
 *
 * @memberOf Document
 */
Document.prototype.addImport = function (newImport) {
    let imports = this.imports;
    let index = imports.indexOf(newImport);
    if (index === -1) imports.push(newImport);
};

/**
 * Remove import
 * @param {Import} removeImport
 *
 * @memberOf Document
 */
Document.prototype.removeImport = function (removeImport) {
    let imports = this.imports;
    let index = imports.indexOf(removeImport);
    if (index !== -1) imports.splice(index, 1);
};

/**
 * Add new Enum type
 * @param {Enum} newEnum
 *
 * @memberOf Document
 */
Document.prototype.addEnum = function (newEnum) {
    let enums = this.enums;
    let index = enums.indexOf(newEnum);
    if (index === -1) enums.push(newEnum);
};

/**
 *
 * @param {Enum} removeEnum
 *
 * @memberOf Document
 */
Document.prototype.removeEnum = function (removeEnum) {
    let enums = this.enums;
    let index = enums.indexOf(removeEnum);
    if (index !== -1) enums.splice(index, 1);
};

/**
 * Add new Message type
 * @param {Message} newMessage
 *
 * @memberOf Document
 */
Document.prototype.addMessage = function (newMessage) {
    let messages = this.messages;
    let index = messages.indexOf(newMessage);
    if (index === -1) messages.push(newMessage);
};

/**
 * Remove Message type
 * @param removeMessage
 *
 * @memberOf Document
 */
Document.prototype.removeMessage = function (removeMessage) {
    let messages = this.messages;
    let index = messages.indexOf(removeMessage);
    if (index !== -1) messages.splice(index, 1);
};

module.exports = Document;



