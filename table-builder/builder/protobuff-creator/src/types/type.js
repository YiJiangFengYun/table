/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type for message filed.
 */
let Base = require("../base");

let Type = function (name, option) {
    Base.call(this, name, option);
};

Object.assign(Type.prototype, Base.prototype, {
    toText:function () {
        return this.name;
    }
});

module.exports = Type;