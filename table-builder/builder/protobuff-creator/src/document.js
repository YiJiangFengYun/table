/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Document Type
 */
let Base = require("./base");
let Syntax = require("./syntax");
let docVersion = require("./documentVersion");

let Document = function (name, version, option) {
    Base.call(this, name, option);
    docVersion.currVersion = version || docVersion.VERSION_3;
    this.syntax = new Syntax("syntax");
};

Object.assign(Document.prototype, Base.prototype, {
   toText:function () {

   }
});

module.exports = Document;



