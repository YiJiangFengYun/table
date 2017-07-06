/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Syntax Type
 */

let Base = require("./base");

let Syntax = function (name, option) {
    Base.call(this, name, option);
    this.version = option ? option.syntax || option.version || "proto3" : "proto3";
};

Object.assign(Syntax.prototype, Base.prototype, {
    toText:function () {
        return "syntax = \"" + this.version + "\";" ;
    }
});