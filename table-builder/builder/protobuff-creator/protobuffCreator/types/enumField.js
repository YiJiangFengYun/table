/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Enum field type for enum definition.
 */

let Base = require("./../base");

let EnumField = function (name, option) {
    Base.call(this, name, option);
    this.number = option ? option.number || 0 : 0;
};

EnumField.prototype = Object.create(Base.prototype);
EnumField.prototype.constructor = EnumField;

EnumField.toText = function () {
    return this.name + " = " + this.number + ";"
};

module.exports = EnumField;
