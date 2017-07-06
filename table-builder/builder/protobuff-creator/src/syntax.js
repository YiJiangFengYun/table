/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Syntax Type
 */

let Base = require("./base");
let docVersion = require("./documentVersion");

let Syntax = function (name, option) {
    Base.call(this, name, option);
    this.version = docVersion.CURR_VERSION === docVersion.VERSION_3 ? "proto3" : "proto2";
};

Object.assign(Syntax.prototype, Base.prototype, {
    toText:function () {
        return "syntax = \"" + this.version + "\";" ;
    }
});