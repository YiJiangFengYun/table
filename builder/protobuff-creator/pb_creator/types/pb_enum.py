from typing import List
from typing import Dict
from pb_creator.types import pb_type
from pb_creator.types import pb_enum_field


class Enum(pb_type.Type):
    def __init__(self, name: str):
        super(Enum, self).__init__(name)
        self.arr_fields: List[pb_enum_field.EnumField] = []

    def add_field(self, field_name: str):
        new_field = pb_enum_field.EnumField(field_name)
        arr_fields = self.arr_fields
        new_field.number = len(arr_fields)
        arr_fields.append(new_field)

    def to_text(self) -> str:
        is_format = False
        result = "enum " + self.name
        if is_format:
            result += "\n"
        result += "{ "
        if is_format:
            result += "\n"
        arr_fields = self.arr_fields
        for field in arr_fields:
            result += field.name + " = " + str(field.number) + ";"
            if is_format:
                result += "\n"
        result += " }"
        return result
