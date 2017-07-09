/**
 * Created by YiJiangFengYun on 2017/7/8.
 * test proto buffer creator.
 */

let protobuffCreator = require("./../protobuff-creator");

let doc = protobuffCreator.createDoc("protobuff-creator-test",
    protobuffCreator.docVersion.VERSION_3,
    "test");

let import1 = protobuffCreator.createImport("import1-test");
let enum1 = protobuffCreator.createEnum("enum1-test");
let message1 = protobuffCreator.createMessage("message1-test");

doc.addImport(import1);
doc.addEnum(enum1);
doc.addMessage(message1);

console.log("document to text: ");
console.log(doc.toText({isFormat: true}));

doc.dispose();

console.log("process end.");