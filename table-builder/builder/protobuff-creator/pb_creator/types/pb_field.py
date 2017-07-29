from pb_creator import base
from pb_creator.types import pb_type

DocType = pb_type.Type


class Field(base.Base):
    def __init__(self, field_name: str, field_type: pb_type.Type, field_option: dict = None):
        super(Field, self).__init__(field_name, field_option)
        self.is_repeated: bool = False
        if field_option is not None and "is_repeated" in field_option:
            self.is_repeated = field_option["is_repeated"]
        self.number: int = 0
        if field_option is not None and "number" in field_option:
            self.number = field_option["number"]
        self.type: DocType = field_type

    def to_text(self, option: dict) -> str:
        result = ""
        if self.is_repeated:
            result += "repeated "
        result += self.type.name + " "
        result += self.name + " = "
        result += str(self.number) + ";"
        return result
