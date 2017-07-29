from pb_creator import base


class Type(base.Base):
    def __init__(self, name: str, option: dict = None):
        super(Type, self).__init__(name, option)

    def to_text(self, option: dict) -> str:
        return self.name
