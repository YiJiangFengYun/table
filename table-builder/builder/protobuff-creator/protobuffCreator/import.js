/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Import Type
 */

let Base = require("./base");

let Import = function (name, option) {
    Base.call(this, name, option);

    this.mode = option ? option.mode || "" : "";
};

Import.prototype = Object.create(Base.prototype);
Import.prototype.constructor = Import;

Import.prototype.toText = function (option) {
    return "import " +
        (this.mode && this.mode !== "" ? this.mode + " " : "") +
        this.name +
        ";";
};

module.exports = Import;
