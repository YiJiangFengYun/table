/**
 * Created by YiJiangFengYun on 2017/7/7.
 * Class Package.
 */

let Base = require("./base");

/**
 * Package type
 * @param {string} name
 * @param {object?} option
 *
 * @constructor
 */
let Package = function (name, option) {
    Base.call(this, name, option);
};

Package.prototype = Object.create(Base.prototype);
Package.prototype.constructor = Package;

/**
 * Create text
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Package
 * @instance
 */
Package.prototype.toText = function (option) {
    return "package " + this.name + ";";
};

module.exports = Package;