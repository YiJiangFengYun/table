/**
 * Created by YiJiangFengYun on 2017/7/8.
 * test proto buffer creator.
 */

let protobuffCreator = require("./../protobuff-creator");

let doc = protobuffCreator.createDoc("protobuff-creator-test",
    protobuffCreator.docVersion.VERSION_3,
    "test");

let buildInTypeMap = protobuffCreator.buildInTypeMap;

let import1 = doc.addImport("import1-test");
let enum1 = doc.addEnum("enum1-test");
let message1 = doc.addMessage("message1-test");

enum1.addField("ENUM_1");
message1.addField("name", buildInTypeMap.string);

console.log("document to text: ");
console.log(doc.toText({isFormat: true}));

doc.dispose();

console.log("process end.");