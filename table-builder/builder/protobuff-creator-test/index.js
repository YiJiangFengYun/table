/**
 * Created by YiJiangFengYun on 2017/7/8.
 * test proto buffer creator.
 */

let protobuffCreator = require("./../protobuff-creator");

let doc = protobuffCreator.createDoc("protobuff-creator-test",
    protobuffCreator.docVersion.VERSION_3,
    "test",
    {isFormat: true});

console.log("document to text: ");
console.log(doc.toText());

doc.dispose();

console.log("process end.");