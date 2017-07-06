/**
 * Created by YiJiangFengYun on 2017/7/6.
 */
var Base = require("../base");

var Type = function (name, option) {
    Base.call(this, name, option);
};

Object.assign(Type.prototype, Base.prototype, {
    toText:function () {
        return "Type";
    }
});

module.exports = Type;