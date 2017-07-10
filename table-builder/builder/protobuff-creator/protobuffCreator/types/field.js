/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Field type of message
 */

let Base = require("./../base");
let Type = require("./type");

/**
 * Field type of message
 * @param {String} name
 * @param {Type} type
 * @param {Object?} option
 *
 * @constructor
 */
let Field = function (name, type, option) {
    Base.call(this, name, option);
    /**
     * @member {Boolean}
     */
    this.isRepeated = option ? option.isRepeated || false : false;
    /**
     * @member {Number}
     */
    this.number = option ? option.number || 0 : 0;
    /**
     * @member {Type}
     */
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