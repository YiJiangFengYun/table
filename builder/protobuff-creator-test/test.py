from os import path
import sys
file_dir = path.dirname(__file__)
sys.path.append(path.join(file_dir, "../protobuff-creator"))

from pb_creator import pb_document
from pb_creator import pb_enum_doc_versions
from pb_creator.types import pb_build_in_types

doc: pb_document.Document = pb_document.Document("protobuff-creator-test",
                                                 pb_enum_doc_versions.DocVersion.VERSION_3,
                                                 "test")

import1 = doc.add_import("import1-test")
enum1 = doc.add_enum("enum1-test")
message1 = doc.add_message("message1-test")

enum1.add_field("ENUM_1")
message1.add_field("field", pb_build_in_types.type_string)
message1.add_field("field2", pb_build_in_types.type_int32)
message1.add_field("field3", pb_build_in_types.type_bytes)
message1.add_field("field4", pb_build_in_types.type_double)
message1.add_field("fieldRepeat", pb_build_in_types.type_int32, True)

message1.add_one_of_group("oneof1", ["field", "field2"])
message1.add_one_of_group("oneof2", ["field3", "field4"])

message2 = doc.add_message("message2-test")
message2.add_field("enum1", enum1)
message2.add_map_field("map1", pb_build_in_types.type_string, pb_build_in_types.type_double)
message2.add_map_field("map2", pb_build_in_types.type_int32, pb_build_in_types.type_string)

print("document to text: ")
print(doc.to_text())

doc.dispose()

print("process end.")
