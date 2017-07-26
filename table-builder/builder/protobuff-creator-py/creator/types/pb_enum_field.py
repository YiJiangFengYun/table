from creator import base


class EnumField(base.Base):
    def __init__(self, name: str, option: dict = None):
        super(EnumField, self).__init__(name, option)
        self.number = 0
        if option is not None and "number" in option:
            self.number = option["number"] or 0

    def to_text(self, option: dict) -> str:
        return self.name + " = " + str(self.number) + ";"
