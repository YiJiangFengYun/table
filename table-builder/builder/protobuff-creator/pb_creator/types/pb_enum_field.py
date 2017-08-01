from pb_creator import base


class EnumField(base.Base):
    def __init__(self, name: str, number: int = 0):
        super(EnumField, self).__init__(name)
        self.number = number

    def to_text(self) -> str:
        return self.name + " = " + str(self.number) + ";"
