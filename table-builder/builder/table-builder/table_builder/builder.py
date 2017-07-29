from typing import List
from table_builder import extensions
from pb_creator import pb_document
from pb_creator import pb_enum_doc_versions
from pb_creator.types import pb_build_in_types
from table_builder import code_creator


class Builder:
    arr_extensions: List[extensions.Base] = []

    def __init__(self,
                 pb_version: int,
                 excels_dir: str = ".",
                 code_output_dir: str = ".",
                 binary_output_dir: str = ".",
                 protoc_path: str = "."):
        self.pb_version: pb_enum_doc_versions.DocVersion = pb_enum_doc_versions.DocVersion(pb_version)
        self.excels_dir: str = excels_dir
        self.code_output_dir: str = code_output_dir
        self.binary_output_dir: str = binary_output_dir
        self.protoc_path: str = protoc_path

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

    def _load_and_build_tables(self):
        """load excel tables in specific location, parse them with _parse_table method"""

        # self._parse_table()
        # self._build_table_pb()
        # self._create_table_objects()
        # self._check_table()
        # self._generate_table_binary()
        pass

    def _parse_table(self):
        """parse table to data arrays"""

    def _build_table_pb(self):
        pass

    def _create_table_objects(self):
        pass

    def _check_table(self):
        pass

    def _generate_table_binary(self):
        pass
