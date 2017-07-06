/**
 * Created by YiJiangFengYun on 2017/7/6.
 */

var Base = require("./base");

var Import = function (name, definition, option) {
    Base.call(this, name, option);
    this.mode = option ? option.mode || "" : "";
    this.definition = definition;
};

Object.assign(Import.prototype, Base.prototype, {
    toText: function () {
        if (!this.definition) throw new Error("The definition is invalid in Import.");
        return "import " +
            (this.mode && this.mode !== "" ? this.mode + " " : "") +
            this.definition +
            ";";
    }
});

module.exports = Import;
