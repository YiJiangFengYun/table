/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type
 */

let Base = function (name, option) {
    this.name = name;
    if (option) {
    }
};

Object.assign(Base.prototype, {
    toText: function () {
        return "Base";
    }
});

module.exports = Base;