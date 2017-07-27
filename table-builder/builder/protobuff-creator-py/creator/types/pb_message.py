from typing import List
from typing import Dict
from creator.types import pb_type
from creator.types import pb_field


class Message(pb_type.Type):
    def __init__(self, name: str, option: Dict = None):
        super(Message, self).__init__(name, option)
        self.arr_fields: List[pb_field.Field] = []
        self.map_fields: Dict[str, pb_field.Field] = {}

    def add_field(self, field_name: str, field_type: pb_type.Type, field_option: dict = None) -> pb_field.Field:
        self.remove_field(field_name)
        new_field = pb_field.Field(field_name, field_type, field_option)
        arr_fields = self.arr_fields
        # start from 1
        new_field.number = len(arr_fields) + 1
        arr_fields.append(new_field)
        self.map_fields[field_name] = new_field
        return new_field

    def remove_field(self, field_name: str) -> pb_field.Field:
        map_fields = self.map_fields
        field_item = None
        if field_name in map_fields:
            field_item = map_fields[field_name]
            self.arr_fields.remove(field_item)
            del map_fields[field_name]
        return field_item

    def to_text(self, option: dict) -> str:
        is_format = False
        if option is not None and "is_format" in option:
            is_format = option["is_format"]
        result = "message " + self.name
        if is_format:
            result += "\n"
        result += " { "
        if is_format:
            result += "\n"
        arr_fields = self.arr_fields
        for field_item in arr_fields:
            result += field_item.to_text(option)
            if is_format:
                result += "\n"
        result += " }"
        return result
