/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type for message filed.
 */
let Base = require("./../base");

let Type = function (name, option) {
    Base.call(this, name, option);
};

Type.prototype = Object.create(Base.prototype);
Type.prototype.constructor = Type;

Type.prototype. toText = function () {
    return this.name;
};

module.exports = Type;