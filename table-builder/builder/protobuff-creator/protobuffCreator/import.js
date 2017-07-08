/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Import Type
 */

let Base = require("./base");

/**
 * Import type
 * @param {string} name
 * @param {string} definition File name for definitions
 * @param {object?} option
 *
 * @class
 * @constructor
 */
let Import = function (name, definition, option) {
    Base.call(this, name, option);
    this.mode = option ? option.mode || "" : "";
    this.definition = definition;
};

Import.prototype = Object.create(Base.prototype);
Import.prototype.constructor = Import;

/**
 * create text
 * @return {string}
 *
 * @memberOf Import
 */
Import.prototype.toText = function () {
    if (!this.definition) throw new Error("The definition is invalid in Import.");
    return "import " +
        (this.mode && this.mode !== "" ? this.mode + " " : "") +
        this.definition +
        ";";
};

module.exports = Import;
