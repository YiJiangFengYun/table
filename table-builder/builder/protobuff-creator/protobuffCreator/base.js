/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type
 */

/**
 * Base type
 *
 * @constructor
 */
let Base = function (name, option) {
    /**
     * @member {String}
     */
    this.name = name;
    if (option) {
    }
};

/**
 * Create text
 * @param {{isFormat:Boolean}} [option]
 * @return {string}
 *
 * @memberOf Base
 * @instance
 */
Base.prototype.toText = function (option) {
    return "Base";
};

module.exports = Base;