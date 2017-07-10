/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Document Type
 */
let Base = require("./base");
let Syntax = require("./syntax");
let Package = require("./package");
let Import = require("./import");
let Enum = require("./types/enum");
let Message = require("./types/message");
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
     * @member {Array.<Import>}
     */
    this.imports = [];
    /**
     * @member {Object.<String, Import>}
     */
    this.importMap = {};
    /**
     *
     * @member {Array.<Import>}
     */
    this.enums = [];
    /**
     *
     * @member {Object.<String, Import>}
     */
    this.enumMap = {};
    /**
     * @member {Array.<Message>}
     */
    this.messages = [];
    /**
     *
     * @member {Object.<String, Message>}
     */
    this.messageMap = {};
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
    delete this.version;
    delete this.syntax;
    delete this.package;
    delete this.imports;
    delete this.importMap;
    delete this.enums;
    delete this.enumMap;
    delete this.messages;
    delete this.messageMap;
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
    let isFormat = option && option.isFormat || false;
    let isNeedNewLine = false;
    let resultStr = "";
    let len;
    let i;

    //syntax
    resultStr += this.syntax.toText(option);

    if (isFormat) resultStr += "\n";

    //package
    resultStr += this.package.toText(option);
    isNeedNewLine = true;

    //imports
    let imports = this.imports;
    len = imports.length;

    if (isFormat && isNeedNewLine && len !== 0) {
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

    if (isFormat && isNeedNewLine && len !== 0) {
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

    if (isFormat && isNeedNewLine && len !== 0) {
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
 * @param {String} name name of import
 * @param {Object?} option
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addImport = function (name, option) {
    this.removeImport(name);
    let imp = new Import(name, option);
    this.imports.push(imp);
    this.importMap[name] = imp;
};

/**
 * Remove import
 * @param {String} name  name of import
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeImport = function (name) {
    let imp = this.importMap[name];
    if (imp) {
        delete this.importMap[name];
        this.imports.splice(this.imports.indexOf(imp));
    }
};

/**
 * Add new Enum type
 * @param {String} name name of enum type
 * @param {Object?} option
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addEnum = function (name, option) {
    this.removeEnum(name);
    let newEnum = new Enum(name, option);
    this.enumMap[name] = newEnum;
    this.enums.push(newEnum);
};

/**
 *
 * @param {String} name
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeEnum = function (name) {
    let e = this.enumMap[name];
    if (e) {
        delete this.enumMap[name];
        this.enums.splice(this.enums.indexOf(e));
    }
};

/**
 * Add new Message type
 * @param {String} name name of message type.
 * @param {Object?} option
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.addMessage = function (name, option) {
    this.removeMessage(name);
    let message = new Message(name, option);
    this.messageMap[name] = message;
    this.messages.push(message);
};

/**
 * Remove Message type
 * @param {String} name name of message type
 * @return void
 *
 * @memberOf Document
 * @instance
 */
Document.prototype.removeMessage = function (name) {
    let message = this.messageMap[name];
    if(message){
        delete this.messageMap[name];
        this.messages.splice(this.messages.indexOf(message));
    }
};

module.exports = Document;



