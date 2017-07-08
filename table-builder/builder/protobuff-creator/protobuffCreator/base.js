/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Base Type
 */

/**
 * Base type
 * @class
 * @constructor
 */
let Base = function (name, option) {
    this.name = name;
    if (option) {
    }
};

/**
 *
 * @return {string}
 *
 * @memberOf Base
 */
Base.prototype.toText = function () {
    return "Base";
};

module.exports = Base;