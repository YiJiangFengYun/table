from pb_creator import base


class Import(base.Base):
    def __init__(self, name: str, mode: str = ""):
        super(Import, self).__init__(name)
        self.mode = mode

    def to_text(self) -> str:
        result_str = "import "
        if self.mode != "":
            result_str += self.mode + " "
        result_str += "\"" + self.name + "\"" + ";"
        return result_str
