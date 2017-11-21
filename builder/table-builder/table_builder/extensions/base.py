from typing import Any
from typing import List

from xlrd.sheet import Sheet

from pb_creator import pb_document


class Base:
    def __init__(self):
        pass

    def on_post_create_table_pb_doc(self, doc: pb_document.Document):
        pass

    def on_post_create_table_obj(self, table_obj: Any, sheet: Sheet):
        pass

    def on_post_create_column_objs(self, arr_col_objs: List, sheet: Sheet):
        pass

    def on_post_create_sheet_pb_doc(self, doc: pb_document.Document):
        pass

    def on_post_create_item_objs(self, arr_item_objs: List, sheet: Sheet):
        pass
