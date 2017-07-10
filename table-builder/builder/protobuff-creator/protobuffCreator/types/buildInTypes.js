/**
 * Created by YiJiangFengYun on 2017/7/6.
 * Collecting build in types
 */

let Type = require("./type");

/**
 *
 * @type {{double: Type,
 *         float: Type,
 *         int32: Type,
 *         int64: Type,
 *         uint32: Type,
 *         uint64: Type,
 *         sint32: Type,
 *         sint64: Type,
 *         fixed32: Type,
 *         fixed64: Type,
 *         sfixed32: Type,
 *         sfixed64: Type,
 *         bool: Type,
 *         string: Type,
 *         bytes: Type}}
 */
let buildInTypeMap = {
    double: new Type("double"),
    float: new Type("float"),
    int32: new Type("int32"),
    int64: new Type("int64"),
    uint32: new Type("uint32"),
    uint64: new Type("uint64"),
    sint32: new Type("sint32"),
    sint64: new Type("sint64"),
    fixed32: new Type("fixed32"),
    fixed64: new Type("fixed64"),
    sfixed32: new Type("sfixed32"),
    sfixed64: new Type("sfixed64"),
    bool: new Type("bool"),
    string: new Type("string"),
    bytes: new Type("bytes")
};

module.exports = buildInTypeMap;