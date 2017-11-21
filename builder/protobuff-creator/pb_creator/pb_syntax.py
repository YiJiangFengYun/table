from pb_creator import base
from pb_creator.pb_enum_doc_versions import DocVersion


class Syntax(base.Base):
    def __init__(self, name: str, version: DocVersion = DocVersion.VERSION_3):
        super(Syntax, self).__init__(name)
        if version == DocVersion.VERSION_3:
            self.version = "proto3"
        else:
            raise ValueError("Syntax version error.")

    def to_text(self) -> str:
        return "syntax = \"" + self.version + "\";"
