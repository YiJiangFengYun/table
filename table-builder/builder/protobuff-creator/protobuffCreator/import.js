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
 * @constructor
 */
let Import = function (name, option) {
    Base.call(this, name, option);
    /**
     * @member {String}
     */
    this.mode = option ? option.mode || "" : "";
};

Import.prototype = Object.create(Base.prototype);
Import.prototype.constructor = Import;

/**
 * Create text
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Import
 * @instance
 */
Import.prototype.toText = function (option) {
    return "import " +
        (this.mode && this.mode !== "" ? this.mode + " " : "") +
        this.name +
        ";";
};

module.exports = Import;
