/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Enum type
 */

let Type = require("./type");
let EnumField = require("./enumField");

/**
 *
 * @param name  enum name
 * @param option enum option
 *
 * @constructor
 */
let Enum = function (name, option) {
    Type.call(this, name, option);
    this.fields = [];
};

Enum.prototype = Object.create(Type.prototype);
Enum.prototype.constructor = Enum;

/**
 *
 * @param {string} fieldName
 * @param {object?} fieldOption
 *
 * @memberOf Enum
 * @instance
 */
Enum.prototype.addField = function (fieldName, fieldOption) {
    let newField = new EnumField(fieldName, fieldOption);
    let fields = this.fields;
    newField.number = fields.length; //start from 0.
    fields.push(newField);
};

/**
 *
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Enum
 * @instance
 */
Enum.prototype.toText = function (option) {
    let result = "enum " + this.name + " { ";
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

module.exports = Enum;
