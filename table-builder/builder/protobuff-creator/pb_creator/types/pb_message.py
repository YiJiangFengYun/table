from typing import List
from typing import Dict
from pb_creator.types import pb_type
from pb_creator.types import pb_field


class Message(pb_type.Type):
    def __init__(self, name: str):
        super(Message, self).__init__(name)
        self.arr_fields: List[pb_field.Field] = []
        self.map_fields: Dict[str, pb_field.Field] = {}
        self.arr_one_of_group: List[List[str]] = []
        self.map_one_of_group: Dict[str, List[str]] = {}

    def add_field(self, field_name: str, field_type: pb_type.Type, is_repeated: bool = False,
                  number: int = 0) -> pb_field.Field:
        self.remove_field(field_name)
        new_field: pb_field.Field = pb_field.Field(field_name, field_type, is_repeated=is_repeated)
        arr_fields = self.arr_fields
        if number == 0:
            # start from 1
            new_field.number = len(arr_fields) + 1
        else:
            new_field.number = number
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

    def add_one_of_group(self, name: str, field_names: List[str]):
        # check field name is exist.
        for field_name in field_names:
            is_exist = False
            for field in self.arr_fields:
                if field_name == field.name:
                    is_exist = True
                    break
            if is_exist is False:
                raise ValueError("Field name specified is not exist.")

        # check field name is repeated in field_names
        field_names_copy = field_names.copy()
        for field_name in field_names:
            is_exist = False
            field_names_copy.remove(field_name)
            for field_name2 in field_names_copy:
                if field_name == field_name2:
                    is_exist = True
                    break
            if is_exist is True:
                raise ValueError("Field name is repeated in field_names argument.")

        # check field name is repeated with one of group has added.from
        for field_name in field_names:
            is_exist = False
            for group_field_names in self.arr_one_of_group:
                for field_name2 in group_field_names:
                    if field_name == field_name2:
                        is_exist = True
                        break
                if is_exist is True:
                    break
            if is_exist is True:
                raise ValueError("Field name is repeated with field names of oneOf group has added to this message.")

        self.remove_one_of_group(name)
        group = field_names.copy()
        self.arr_one_of_group.append(group)
        self.map_one_of_group[name] = group

    def remove_one_of_group(self, name: str):
        map_one_of_group = self.map_one_of_group
        if name in map_one_of_group:
            one_of_group = self.map_one_of_group[name]
            self.arr_one_of_group.remove(one_of_group)
            del map_one_of_group[name]

    def to_text(self) -> str:
        result = "message " + self.name
        result += " { "

        arr_fields_copy = self.arr_fields.copy()
        map_fields = self.map_fields

        for one_of_name, group in self.map_one_of_group.items():
            result += "oneof " + one_of_name + " { "

            for field_name in group:
                field_item = map_fields[field_name]
                result += field_item.to_text()
                arr_fields_copy.remove(field_item)

            result += " } "

        for field_item in arr_fields_copy:
            result += field_item.to_text()
        result += " }"
        return result
