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

let Document = function (name, version, packageName, option) {
    Base.call(this, name, option);

    this.version = version || docVersion.VERSION_3;

    this.syntax = new Syntax("documentSyntax", {version: this.version});

    this.package = new Package(packageName);

    this.imports = [];

    this.importMap = {};

    this.enums = [];

    this.enumMap = {};

    this.messages = [];

    this.messageMap = {};
};

Document.prototype = Object.create(Base.prototype);
Document.prototype.constructor = Document;

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
        resultStr += "\n";
        isNeedNewLine = false;
    }

    for (i = 0; i < len; ++i) {
        resultStr += enums[i].toText(option);
        resultStr += "\n";
        isNeedNewLine = false;
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
        resultStr += "\n";
        isNeedNewLine = false;
    }

    isNeedNewLine = false;
    return resultStr;

};

Document.prototype.addImport = function (name, option) {
    this.removeImport(name);
    let imp = new Import(name, option);
    this.imports.push(imp);
    this.importMap[name] = imp;

    return imp;
};

Document.prototype.removeImport = function (name) {
    let imp = this.importMap[name];
    if (imp) {
        delete this.importMap[name];
        this.imports.splice(this.imports.indexOf(imp));
    }
    return imp;
};

Document.prototype.addEnum = function (name, option) {
    this.removeEnum(name);
    let newEnum = new Enum(name, option);
    this.enumMap[name] = newEnum;
    this.enums.push(newEnum);
    return newEnum;
};

Document.prototype.removeEnum = function (name) {
    let e = this.enumMap[name];
    if (e) {
        delete this.enumMap[name];
        this.enums.splice(this.enums.indexOf(e));
    }
    return e;
};

Document.prototype.addMessage = function (name, option) {
    this.removeMessage(name);
    let message = new Message(name, option);
    this.messageMap[name] = message;
    this.messages.push(message);
    return message;
};

Document.prototype.removeMessage = function (name) {
    let message = this.messageMap[name];
    if(message){
        delete this.messageMap[name];
        this.messages.splice(this.messages.indexOf(message));
    }
    return message;
};

module.exports = Document;



