/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Message type
 */

let Type = require("./type");
let Field = require("./field");

/**
 *
 * @param {string} name
 * @param {object?} option
 *
 * @constructor
 */
let Message = function (name, option) {
    Type.call(name, option);
    this.fields = [];
};

Message.prototype = Object.create(Type.prototype);
Message.prototype.constructor = Message;

/**
 * Add filed to message.
 * @param {string} fieldName
 * @param {Type} fieldType
 * @param {object?} fieldOption
 *
 * @memberOf Message
 * @instance
 */
Message.prototype.addField = function (fieldName, fieldType, fieldOption) {
    let newField = new Field(fieldName, fieldType, fieldOption);
    let fields = this.fields;
    newField.number = fields.length + 1; //start from 1.
    fields.push(newField);
};

/**
 * create text
 * @return {string}
 *
 * @memberOf Message
 * @instance
 */
Message.prototype.toText = function () {
    let result = "message " + this.name + " { ";
    let fields = this.fields;
    let len = fields.length;
    let i;
    for(i = 0; i < len; ++i)
    {
        result += fields[i].name + " = " + fields[i].number + ";";
    }
    result += " }";
    return result;

};

module.exports = Message;
