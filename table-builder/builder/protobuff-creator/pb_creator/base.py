class Base:
    def __init__(self, name: str, option: dict = None):
        self.name = name

    def to_text(self, option: dict) -> str:
        return self.name

