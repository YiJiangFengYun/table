/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Enum type
 */

let Type = require("./type");
let EnumField = require("./enumField");

let Enum = function (name, option) {
    Type.call(this, name, option);
    this.fields = [];
};

Object.assign(Enum.prototype, Type.prototype, {
    addField: function (fieldName, fieldOption) {
        let newField = new EnumField(fieldName, fieldOption);
        let fields = this.fields;
        newField.number = fields.length; //start from 0.
        fields.push(newField);
    },
    toText: function () {
        //todo
    }
});

module.exports = Enum;
