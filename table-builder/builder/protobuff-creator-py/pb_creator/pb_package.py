from pb_creator import base


class Package(base.Base):
    def __init__(self, name: str, option: dict = None):
        super(Package, self).__init__(name, option)

    def to_text(self, option: dict) -> str:
        return "package " + self.name + ";"
