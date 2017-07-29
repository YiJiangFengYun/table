from pathlib import Path
from typing import List

import xlrd

from pb_creator import pb_document
from pb_creator import pb_enum_doc_versions
from pb_creator.types import pb_build_in_types
from table_builder import code_creator
from table_builder import extensions


class Builder:
    arr_extensions: List[extensions.Base] = []

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

        self.pb_version: pb_enum_doc_versions.DocVersion = pb_enum_doc_versions.DocVersion(pb_version)
        self.excels_dir: Path = excels_dir
        self.code_output_dir: Path = code_output_dir
        self.binary_output_dir: Path = binary_output_dir
        self.protoc_path: Path = protoc_path

    def register_extension(self, extension: extensions.Base):
        self.arr_extensions.index(extension)
        pass

    def build(self):
        self._build_common_pb()
        self._load_and_build_tables()
        pass

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

        creator = code_creator.CodeCreator(self.code_output_dir, self.protoc_path)
        creator.create(table_pb_doc)

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
                book = xlrd.open_workbook(str(path))
                self._parse_table(book)
                self._build_table_pb()
                self._create_table_objects()
                self._check_table()
                self._generate_table_binary()

    def _parse_table(self, book: xlrd.Book):
        """parse table to data arrays"""
        num_work_sheets = book.nsheets
        if num_work_sheets < 3:
            raise Exception("Num of Excel sheets less than 3!")

    def _build_table_pb(self):
        pass

    def _create_table_objects(self):
        pass

    def _check_table(self):
        pass

    def _generate_table_binary(self):
        pass
