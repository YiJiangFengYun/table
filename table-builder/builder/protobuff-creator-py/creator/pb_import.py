from creator import base


class Import(base.Base):
    def __init__(self, name: str, option: dict = None):
        super(Import, self).__init__(name, option)
        self.mode = ""
        if option is not None and "mode" in option:
            self.mode = option["mode"]

    def to_text(self, option: dict) -> str:
        result_str = "import "
        if self.mode != "":
            result_str += self.mode + " "
        result_str += self.name + ";"
        return result_str
