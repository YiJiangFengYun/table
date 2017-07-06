/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Document Type
 */
let Base = require("./base");

let ProtoBuffDoc = function (name, option) {
    Base.call(this, name, option);
    this.syntax = option && option.syntax ? option.syntax : "proto3";
    this.package = option && option.package ? option.package : "";

};

Object.assign(ProtoBuffDoc.prototype, Base.prototype, {
   toText:function () {

   }
});

module.exports = ProtoBuffDoc;



