from pb_creator import base


class Type(base.Base):
    def __init__(self, name: str):
        super(Type, self).__init__(name)

    def to_text(self) -> str:
        return self.name
