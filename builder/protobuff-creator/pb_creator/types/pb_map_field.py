from pb_creator.types import pb_field
from pb_creator.types import pb_type


class MapField(pb_field.Field):
    def __init__(self, field_name: str, key_type: pb_type.Type, field_type: pb_type.Type, number: int = 0, ):
        super(MapField, self).__init__(field_name, field_type, number, False)
        self.key_type = key_type

    def to_text(self) -> str:
        result = "map<"
        result += self.key_type.name + ", "
        result += self.type.name
        result += "> "
        result += self.name
        result += " = "
        result += str(self.number)
        result += ";"
        return result
