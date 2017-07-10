/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Enum field type for enum definition.
 */

let Base = require("./../base");

/**
 *
 * @param {string} name
 * @param {object?} option
 *
 * @constructor
 * @instance
 */
let EnumField = function (name, option) {
    Base.call(this, name, option);
    /**
     * @member {Number}
     */
    this.number = option ? option.number || 0 : 0;
};

EnumField.prototype = Object.create(Base.prototype);
EnumField.prototype.constructor = EnumField;

/**
 *
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf EnumField
 * @instance
 */
EnumField.toText = function (option) {
    return this.name + " = " + this.number + ";"
};

module.exports = EnumField;
