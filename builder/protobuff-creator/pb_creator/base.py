class Base:
    def __init__(self, name: str):
        self.name = name

    def to_text(self) -> str:
        return self.name

