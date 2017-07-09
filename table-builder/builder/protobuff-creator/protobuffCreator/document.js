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
 * @constructor
 */
let Document = function (name, version, packageName, option) {
    Base.call(this, name, option);
    /**
     * @member {Number}
     */
    this.version = version || docVersion.VERSION_3;
    /**
     *
     * @member {Syntax}
     */
    this.syntax = new Syntax("documentSyntax", {version: this.version});
    /**
     *
     * @member {Package}
     */
    this.package = new Package(packageName);

    /**
     *
     * @member {Boolean}
     */
    this.isFormat = option && option.isFormat || false;
    /**
     *
     * @member {Array.<Import>}
     */
    this.imports = [];
    /**
     *
     * @member {Array.<Import>}
     */
    this.enums = [];
    /**
     * @member {Array.<Message>}
     */
    this.messages = [];
};

Document.prototype = Object.create(Base.prototype);
Document.prototype.constructor = Document;

/**
 *
 * @return void
 * @memberOf Document
 * @instance
 * @method
 */
Document.prototype.dispose = function () {
    this.imports.length = 0;
    this.enums.length = 0;
    this.messages.length = 0;
    delete this.version;
    delete this.syntax;
    delete this.package;
    delete this.imports;
    delete this.enums;
    delete this.messages;

};

/**
 * create text
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.toText = function (option) {
    //option isFormat is preferential to member(field) isformat.
    let isFormat = option && option.isFormat !== undefined ? option.isFormat : this.isFormat;
    let isNeedNewLine = false;
    let resultStr = "";
    let len;
    let i;

    //syntax
    resultStr += this.syntax.toText(option);

    if(isFormat)resultStr += "\n";

    //package
    resultStr += this.package.toText(option);
    isNeedNewLine = true;

    //imports
    let imports = this.imports;
    len = imports.length;

    if(isFormat && isNeedNewLine && len !== 0)
    {
        resultStr += "\n";
        isNeedNewLine = false;
    }

    for (i = 0; i < len; ++i) {
        resultStr += imports[i].toText(option);
        isNeedNewLine = true;
    }

    //enums
    let enums = this.enums;
    len = enums.length;

    if(isFormat && isNeedNewLine && len !== 0)
    {
        resultStr += "\n"
        isNeedNewLine = false;
    }

    for (i = 0; i < len; ++i) {
        resultStr += enums[i].toText(option);
        isNeedNewLine = true;
    }

    //messages
    let messages = this.messages;
    len = messages.length;

    if(isFormat && isNeedNewLine && len !== 0)
    {
        resultStr += "\n";
        isFormat = false;
    }

    for (i = 0; i < len; ++i) {
        resultStr += messages[i].toText(option);
        isNeedNewLine = true;
    }

    isNeedNewLine = false;
    return resultStr;

};

/**
 * Add import
 * @param {Import} newImport
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addImport = function (newImport) {
    let imports = this.imports;
    let index = imports.indexOf(newImport);
    if (index === -1) imports.push(newImport);
};

/**
 * Remove import
 * @param {Import} removeImport
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeImport = function (removeImport) {
    let imports = this.imports;
    let index = imports.indexOf(removeImport);
    if (index !== -1) imports.splice(index, 1);
};

/**
 * Add new Enum type
 * @param {Enum} newEnum
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addEnum = function (newEnum) {
    let enums = this.enums;
    let index = enums.indexOf(newEnum);
    if (index === -1) enums.push(newEnum);
};

/**
 *
 * @param {Enum} removeEnum
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeEnum = function (removeEnum) {
    let enums = this.enums;
    let index = enums.indexOf(removeEnum);
    if (index !== -1) enums.splice(index, 1);
};

/**
 * Add new Message type
 * @param {Message} newMessage
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addMessage = function (newMessage) {
    let messages = this.messages;
    let index = messages.indexOf(newMessage);
    if (index === -1) messages.push(newMessage);
};

/**
 * Remove Message type
 * @param {Message} removeMessage
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeMessage = function (removeMessage) {
    let messages = this.messages;
    let index = messages.indexOf(removeMessage);
    if (index !== -1) messages.splice(index, 1);
};

module.exports = Document;



