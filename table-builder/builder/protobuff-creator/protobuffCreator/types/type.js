/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type for message filed.
 */
let Base = require("./../base");

/**
 * Proto buff type
 * @param {string} name
 * @param {object?} option
 *
 * @class
 * @constructor
 */
let Type = function (name, option) {
    Base.call(this, name, option);
};

Type.prototype = Object.create(Base.prototype);
Type.prototype.constructor = Type;

/**
 * @return {string}
 *
 * @memberOf Type
 */
Type.prototype. toText = function () {
    return this.name;
};

module.exports = Type;