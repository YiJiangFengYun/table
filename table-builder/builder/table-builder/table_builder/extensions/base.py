from typing import Any


class Base:
    def __init__(self):
        pass

    def parseSheetCell(self,
                       sheet_index: int,
                       sheet_name: str,
                       col_index: int,
                       col_name: str,
                       row_index: int,
                       cell_value: Any):
        pass
