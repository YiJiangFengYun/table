/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Field type of message
 */

let Base = require("./../base");

let Field = function (name, type, option) {
    Base.call(this, name, option);
    this.isRepeated = option ? option.isRepeated || false : false;
    this.number = option ? option.number || 0 : 0;
    this.type = type;
};

Object.assign(Field.prototype, Base.prototype, {
    toText: function () {
        return (this.isRepeated ? "repeated " : "") +
            this.type.toText() + " " +
            this.name + " = " +
            this.number + ";"
    }
});

module.exports = Field;