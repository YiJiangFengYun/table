from pb_creator import base


class Package(base.Base):
    def __init__(self, name: str):
        super(Package, self).__init__(name)

    def to_text(self) -> str:
        return "package " + self.name + ";"
