from creator import base
from creator.pb_enum_doc_versions import DocVersion


class Syntax(base.Base):
    def __init__(self, name: str, option: dict = None):
        super(Syntax, self).__init__(name, option)
        self.version = "proto3"
        if option is not None and "version" in option and option["version"] == DocVersion.VERSION_2:
            self.version = "proto2"

    def to_text(self, option: dict) -> str:
        return "syntax = \"" + self.version + "\";"
