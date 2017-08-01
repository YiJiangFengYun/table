from pb_creator import base
from pb_creator.pb_enum_doc_versions import DocVersion


class Syntax(base.Base):
    def __init__(self, name: str, version:DocVersion = DocVersion.VERSION_3):
        super(Syntax, self).__init__(name)
        if version == DocVersion.VERSION_2:
            self.version = "proto2"
        else:
            self.version = "proto3"

    def to_text(self) -> str:
        return "syntax = \"" + self.version + "\";"
