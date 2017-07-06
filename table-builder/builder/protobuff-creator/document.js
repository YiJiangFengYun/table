

var ProtoBuffDoc = function (option) {
    this.syntax = option && option.syntax ? option.syntax : "proto3";
    this.package = option && option.package ? option.package : "";

};

module.exports = ProtoBuffDoc;



