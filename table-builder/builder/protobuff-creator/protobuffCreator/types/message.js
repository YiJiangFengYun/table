/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Message type
 */

let Type = require("./type");
let Field = require("./field");

let Message = function (name, option) {
    Type.call(this, name, option);

    this.fields = [];

    this.fieldMap = {};
};

Message.prototype = Object.create(Type.prototype);
Message.prototype.constructor = Message;

Message.prototype.addField = function (fieldName, fieldType, fieldOption) {
    this.removeField(fieldName);
    let newField = new Field(fieldName, fieldType, fieldOption);
    let fields = this.fields;
    newField.number = fields.length + 1; //start from 1.
    fields.push(newField);
    this.fieldMap[fieldName] = newField;

    return newField;
};

Message.prototype.removeField = function (fieldName) {
    let field = this.fieldMap[fieldName];
    if(field)
    {
        this.fields.splice(this.fields.indexOf(field));
        delete this.fieldMap[fieldName];
    }

    return field;
}

Message.prototype.toText = function (option) {
    let isFormat = option && option.isFormat || false;
    let result = "message " + this.name;
    if(isFormat)result += "\n";
    result += " { ";
    if(isFormat)result += "\n";
    let fields = this.fields;
    let len = fields.length;
    let i;
    for(i = 0; i < len; ++i)
    {
        result += fields[i].toText(option);
        if(isFormat)result += "\n";
    }
    result += " }";
    return result;

};

module.exports = Message;

