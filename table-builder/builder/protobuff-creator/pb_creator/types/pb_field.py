from pb_creator import base
from pb_creator.types import pb_type

DocType = pb_type.Type


class Field(base.Base):
    def __init__(self, field_name: str, field_type: pb_type.Type, number: int = 0, is_repeated: bool = False):
        super(Field, self).__init__(field_name)
        self.is_repeated: bool = is_repeated
        self.number: int = number
        self.type: DocType = field_type

    def to_text(self) -> str:
        result = ""
        if self.is_repeated:
            result += "repeated "
        result += self.type.name + " "
        result += self.name + " = "
        result += str(self.number) + ";"
        return result
