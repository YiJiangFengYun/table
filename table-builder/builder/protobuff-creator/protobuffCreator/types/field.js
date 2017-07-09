﻿/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Field type of message
 */

let Base = require("./../base");

/**
 * Field type of message
 * @param {string} name
 * @param {Type} type
 * @param {object?} option
 *
 * @constructor
 */
let Field = function (name, type, option) {
    Base.call(this, name, option);
    this.isRepeated = option ? option.isRepeated || false : false;
    this.number = option ? option.number || 0 : 0;
    this.type = type;
};

Field.prototype = Object.create(Base.prototype);
Field.prototype.constructor = Field;

/**
 *
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Field
 * @instance
 */
Field.prototype.toText = function (option) {
    return (this.isRepeated ? "repeated " : "") +
        this.type.toText() + " " +
        this.name + " = " +
        this.number + ";"
};

module.exports = Field;