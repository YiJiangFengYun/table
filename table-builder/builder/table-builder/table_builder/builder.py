import logging
import os
import typing
from pathlib import Path

import xlrd
from google.protobuf import message

from pb_creator import pb_document
from pb_creator import pb_enum_doc_versions
from pb_creator.types import pb_build_in_types
from pb_creator.types import pb_message
from table_builder import binary_creator
from table_builder import code_creator
from table_builder import extensions


class Builder:
    arr_extensions: typing.List[extensions.Base] = []

    def __init__(self,
                 pb_version: int,
                 excels_dir: Path = ".",
                 code_output_dir: Path = ".",
                 binary_output_dir: Path = ".",
                 protoc_path: Path = "."):
        #  some detects for arguments.
        if excels_dir.exists() is False:
            raise ValueError("Excel directory don't exists!")
        if excels_dir.is_dir() is False:
            raise ValueError("Argument value of excel directory is not a directory!")
        if code_output_dir.exists() is False:
            raise ValueError("Code output directory don't exists!")
        if code_output_dir.is_dir() is False:
            raise ValueError("Argument value of code output directory is not a directory!")
        if binary_output_dir.exists() is False:
            raise ValueError("Binary ouput directory don't exists!")
        if binary_output_dir.is_dir() is False:
            raise ValueError("Argument value of binary output directory is not a directory!")
        if protoc_path.exists() is False:
            raise ValueError("Protoc file specified with protoc_path don't exists!")

        self.pb_version = pb_enum_doc_versions.DocVersion(pb_version)
        self.excels_dir: Path = excels_dir
        self.code_output_dir: Path = code_output_dir
        self.binary_output_dir: Path = binary_output_dir
        self.protoc_path: Path = protoc_path
        self.table_locals: typing.Dict[str, typing.Any] = {}
        self.table_pb_document: pb_document.Document = None
        self.table_module_name: str = None
        self.table_message: pb_message.Message = None
        self.column_message: pb_message.Message = None
        self.table_msg_id: int = 0

        logging.getLogger().setLevel(logging.INFO)

    def register_extension(self, extension: extensions.Base):
        self.arr_extensions.index(extension)
        pass

    def build(self):
        self._build_common_pb()
        self._load_and_build_tables()

    def _build_common_pb(self):
        """build common dynamic proto buffer document, run protoc application to generate
        protocol code for difference languages."""
        package_name = "table"
        table_pb_doc: pb_document.Document = pb_document.Document("table", self.pb_version, package_name)
        table_message = table_pb_doc.add_message("Table")
        table_message.add_field("name", pb_build_in_types.type_string)
        table_message.add_field("description", pb_build_in_types.type_string)

        column_message = table_pb_doc.add_message("Column")
        column_message.add_field("name", pb_build_in_types.type_string)
        column_message.add_field("description", pb_build_in_types.type_string)
        column_message.add_field("type_name", pb_build_in_types.type_string)

        creator: code_creator.CodeCreator = code_creator.CodeCreator(self.code_output_dir, self.protoc_path, self.table_locals)
        self.table_module_name = creator.create(table_pb_doc)

        self.table_pb_document = table_pb_doc
        self.table_message = table_message
        self.column_message = column_message

    def _load_and_build_tables(self, excels_dir: Path = None):
        """load excel tables in specific location, parse them with _parse_table method"""
        if excels_dir is None:
            excels_dir = self.excels_dir
        for child in excels_dir.iterdir():
            path: Path = child
            if path.is_dir():
                self._load_and_build_tables(path)
                continue
            else:
                file_name, file_extension = os.path.splitext(str(path))
                if file_extension == ".xlsx":
                    book = xlrd.open_workbook(str(path))
                    sheet_table_obj = self._parse_table(book)
                    self._check_table(sheet_table_obj)
                    self._generate_table_binary(sheet_table_obj)

    def _parse_table(self, book: xlrd.Book):
        """parse table to table object, and create table pb"""
        num_work_sheets = book.nsheets
        if num_work_sheets < 3:
            raise Exception("Num of Excel sheets less than 3!")

        # first sheet, it should be a sheet of target table attributes
        sheet_index = 0
        sh = book.sheet_by_index(sheet_index)
        logging.info("First sheet, name:{0}, row number: {1}, col number: {2}.".format(sh.name, sh.nrows, sh.ncols))
        table_name = None
        table_description = None
        for col in range(sh.ncols):
            for row in range(sh.nrows):
                if row == 0:
                    attr_name = str(sh.cell_value(row, col))
                elif row == 1 and col == 0:
                    #  table name
                    table_name = str(sh.cell_value(row, col))
                elif row == 1 and col == 1:
                    #  table description
                    table_description = str(sh.cell_value(row, col))
                else:
                    pass
                    # for ext in self.arr_extensions:
                    #     ext.parseSheetCell(sheet_index, sh.name, col, attr_name, row - 1, sh.cell_value(row, col))

        # create table object.
        table_obj = getattr(self.table_locals[self.table_module_name], "Table")()

        if table_name is not None:
            setattr(table_obj, "name", table_name)
        else:
            raise RuntimeError("Table name doesn't exist in Excel. sheet name: {}.".format(sh.name))

        if table_description is not None:
            setattr(table_obj, "description", table_description)
        else:
            raise RuntimeError("Table description doesn't exist in Excel. sheet name: {}.".format(sh.name))

        # second sheet, it should be a sheet of target table column attributes
        sheet_index = 1
        sh = book.sheet_by_index(sheet_index)
        logging.info("Second sheet, name:{0}, row number: {1}, col number: {2}.".format(sh.name, sh.nrows, sh.ncols))
        arr_col_objs: typing.List = []
        for row in range(sh.nrows):
            col_name = None
            col_type_name = None
            col_description = None
            for col in range(sh.ncols):
                if row == 0:
                    attr_name = str(sh.cell_value(row, col))
                else:
                    if col == 0:
                        col_name = str(sh.cell_value(row, col))
                        col_name = col_name.replace(" ", "_")
                    elif col == 1:
                        col_type_name = str(sh.cell_value(row, col))
                    elif col == 2:
                        col_description = str(sh.cell_value(row, col))
                    else:
                        pass

            if row == 0:
                continue
            # create column object.
            column_obj = getattr(self.table_locals[self.table_module_name], "Column")()

            if col_name is not None:
                setattr(column_obj, "name", col_name)
            else:
                raise RuntimeError(
                    "Table column name doesn't exist in Excel, sheet name: {0}, col index: {1}.".format(sh.name,
                                                                                                        row - 1))

            if col_type_name is not None:
                setattr(column_obj, "type_name", col_type_name)
            else:
                raise RuntimeError(
                    "Table column type name doesn't exist in Excel, sheet name: {0}, col index: {1}.".format(
                        sh.name,
                        row - 1))

            if col_description is not None:
                setattr(column_obj, "description", col_description)
            else:
                raise RuntimeError(
                    "Table column description doesn't exist in Excel, sheet name: {0}, col index: {1}.".format(
                        sh.name,
                        row - 1))

            arr_col_objs.append(column_obj)

        sheet_msg_module_name, sheet_table_msg_name, sheet_table_item_msg_name = self._build_table_pb(table_name,
                                                                                                      arr_col_objs)

        #  Third sheet,  it should be a sheet of actual data of target table.
        sheet_index = 2
        sh = book.sheet_by_index(sheet_index)
        logging.info("Third sheet, name:{0}, row number: {1}, col number: {2}.".format(sh.name, sh.nrows, sh.ncols))
        sheet_table_obj = getattr(self.table_locals[sheet_msg_module_name], sheet_table_msg_name)()
        table_field_obj: message.Message = getattr(sheet_table_obj, "table")
        table_field_obj.CopyFrom(table_obj)
        columns_field = getattr(sheet_table_obj, "columns")
        columns_field.extend(arr_col_objs)
        arr_table_items: typing.List = []
        for row in range(sh.nrows):
            table_item = getattr(self.table_locals[sheet_msg_module_name], sheet_table_item_msg_name)()
            for col in range(sh.ncols):
                if row == 0:
                    attr_name = str(sh.cell_value(row, col))
                else:
                    item_field_name = getattr(arr_col_objs[col], "name")
                    item_field_type = type(getattr(table_item, item_field_name))
                    try:
                        item_field_value = item_field_type(sh.cell_value(row, col))
                    except Exception as e:
                        logging.warning(e)
                    else:
                        setattr(table_item, item_field_name, item_field_value)
            arr_table_items.append(table_item)
        items_field = getattr(sheet_table_obj, "items")
        items_field.extend(arr_table_items)
        return sheet_table_obj

    def _build_table_pb(self, table_name: str, arr_col_objs: typing.List):
        """build table dynamic proto buffer document, run protoc application to generate
        protocol code for difference languages."""
        table_name = table_name.replace(" ", "_")  # replace space with underscore.
        package_name = "table"

        # The sheet table document
        pb_doc: pb_document.Document = pb_document.Document(table_name, self.pb_version, package_name)

        # Import Table and Column message definitions
        pb_doc.add_import(self.table_pb_document.name + ".proto")

        #  Create sheet table message definition name
        table_name = table_name[0:1].upper() + table_name[1:]  # convert first char to uppercase
        #  Create sheet table message definition.
        table_message = pb_doc.add_message(table_name)
        #  Add table field to sheet table message.
        table_message.add_field("table", self.table_message)
        #  Add columns field to sheet table message.
        table_message.add_field("columns", self.column_message, True)
        #  Create sheet table item message definition.
        table_item_name = table_name + "Item"
        table_item_message = pb_doc.add_message(table_item_name)
        for col_obj in arr_col_objs:
            col_name: str = getattr(col_obj, "name")
            col_name = col_name.replace(" ", "_")  # replace space with underscore.
            table_item_message.add_field(col_name, pb_build_in_types.map_types[getattr(col_obj, "type_name")])

        # Add items field to sheet table message.
        table_message.add_field("items", table_item_message, True)

        # Create proto file and codes.
        creator = code_creator.CodeCreator(self.code_output_dir, self.protoc_path, self.table_locals)
        module_name = creator.create(pb_doc)

        # Add msg id
        self.table_msg_id += 1

        return module_name, table_name, table_item_name

    def _check_table(self, sheet_table_obj):
        pass

    def _generate_table_binary(self, sheet_table_obj):
        file_creator = binary_creator.BinaryCreator(self.binary_output_dir)
        table_obj = getattr(sheet_table_obj, "table")
        file_name = getattr(table_obj, "name")
        msg: message.Message = sheet_table_obj
        file_creator.create(file_name, msg.SerializePartialToString())
