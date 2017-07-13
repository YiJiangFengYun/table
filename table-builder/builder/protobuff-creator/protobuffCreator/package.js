/**
 * Created by YiJiangFengYun on 2017/7/7.
 * Class Package.
 */

let Base = require("./base");

let Package = function (name, option) {
    Base.call(this, name, option);
};

Package.prototype = Object.create(Base.prototype);
Package.prototype.constructor = Package;

Package.prototype.toText = function (option) {
    return "package " + this.name + ";";
};

module.exports = Package;