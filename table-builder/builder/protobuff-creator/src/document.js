/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Document Type
 */
let Base = require("./base");

let Document = function (name, version, option) {
    Base.call(this, name, option);
};

Object.assign(Document.prototype, Base.prototype, {
   toText:function () {

   }
});

module.exports = Document;



