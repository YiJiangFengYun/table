from creator import base
from creator.types import pb_type

DocType = pb_type.Type


class Field(base.Base):
    def __init__(self, name: str, type: pb_type.Type, option: dict = None):
        super(Field, self).__init__(name, option)
        self.is_repeated = False  # type: bool
        if option is not None and "is_repeated" in option:
            self.is_repeated = option["is_repeated"]
        self.number = 0  # type: int
        if option is not None and "number" in option:
            self.number = option["number"]
        self.type = type  # type: DocType

    def to_text(self, option: dict) -> str:
        result = ""
        if self.is_repeated:
            result += "repeated "
        result += self.type.name + " "
        result += self.name + " = "
        result += str(self.number) + ";"
        return result
