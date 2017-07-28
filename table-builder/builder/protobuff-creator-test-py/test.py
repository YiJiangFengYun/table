from pb_creator import pb_document
from pb_creator import pb_enum_doc_versions
from pb_creator.types import pb_build_in_types

doc = pb_document.Document("protobuff-creator-test",
                           pb_enum_doc_versions.DocVersion.VERSION_3,
                           "test")

import1 = doc.add_import("import1-test")
enum1 = doc.add_enum("enum1-test")
message1 = doc.add_message("message1-test")

enum1.add_field("ENUM_1")
message1.add_field("field", pb_build_in_types.type_string)
message1.add_field("fieldRepeat", pb_build_in_types.type_int32, {"is_repeated": True})

message2 = doc.add_message("message2-test")
message2.add_field("enum1", enum1)

print("document to text: ")
print(doc.to_text())

doc.dispose()

print("process end.")
