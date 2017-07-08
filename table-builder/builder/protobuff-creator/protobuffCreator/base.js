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
    this.name = name;
    if (option) {
    }
};

/**
 *
 * @return {string}
 *
 * @memberOf Base
 * @instance
 */
Base.prototype.toText = function () {
    return "Base";
};

module.exports = Base;