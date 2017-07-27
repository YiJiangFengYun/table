from typing import List
from typing import Dict
from creator import base
from creator import pb_syntax
from creator import pb_package
from creator import pb_import
from creator.types import pb_enum
from creator.types import pb_message
from creator import pb_enum_doc_versions


class Document(base.Base):
    def __init__(self, name: str, version: pb_enum_doc_versions.DocVersion,
                 package_name: str, option: Dict = None):
        super(Document, self).__init__(name, option)
        self.version = version
        self.syntax = pb_syntax.Syntax("documentSyntax", {version: self.version})
        self.package = pb_package.Package(package_name)
        self.arr_imports: List[pb_import.Import] = []
        self.map_imports: Dict[str, pb_import.Import] = {}
        self.arr_enums: List[pb_enum.Enum] = []
        self.map_enums: Dict[str, pb_enum.Enum] = {}
        self.arr_messages: List[pb_message.Message] = []
        self.map_messages: Dict[str, pb_message.Message] = {}

    def dispose(self):
        del self.version
        del self.syntax
        del self.package
        del self.arr_imports
        del self.map_imports
        del self.arr_enums
        del self.map_enums
        del self.arr_messages
        del self.map_messages

    def to_text(self, option: dict = None) -> str:
        if option is None:
            option = {}
        is_format = False
        if option is not None and "is_format" in option:
            is_format = option["is_format"]
        result = ""
        is_need_new_line = False

        # syntax
        result += self.syntax.to_text(option)
        if is_format:
            result += "\n"

        # package
        result += self.package.to_text(option)

        # imports
        arr_imports = self.arr_imports
        arr_len = len(arr_imports)
        if is_need_new_line and arr_len != 0:
            result += "\n"
            is_need_new_line = False
        for import_item in arr_imports:
            result += import_item.to_text(option)
            if is_need_new_line:
                result += "\n"
            if is_format:
                is_need_new_line = True

        # enums
        arr_enums = self.arr_enums
        arr_len = len(arr_enums)
        if is_need_new_line and arr_len != 0:
            result += "\n"
            is_need_new_line = False
        for enum_item in arr_enums:
            result += enum_item.to_text(option)
            if is_need_new_line:
                result += "\n"
            if is_format:
                is_need_new_line = True

        # messages
        arr_messages = self.arr_messages
        arr_len = len(arr_messages)
        if is_need_new_line and arr_len != 0:
            result += "\n"
            is_need_new_line = False
        for message_item in arr_messages:
            result += message_item.to_text(option)
            if is_need_new_line:
                result += "\n"
            if is_format:
                is_need_new_line = True

        is_need_new_line = False
        return result

    def add_import(self, name: str, option: dict = None) -> pb_import.Import:
        self.remove_import(name)
        imp = pb_import.Import(name, option)
        self.arr_imports.append(imp)
        self.map_imports[name] = imp
        return imp

    def remove_import(self, name: str) -> pb_import.Import:
        map_imports = self.map_imports
        imp = None
        if name in map_imports:
            imp = map_imports[name]
            self.arr_imports.remove(imp)
            del map_imports[name]
        return imp

    def add_enum(self, name: str, option: dict = None) -> pb_enum.Enum:
        self.remove_enum(name)
        enum = pb_enum.Enum(name, option)
        self.arr_enums.append(enum)
        self.map_enums[name] = enum
        return enum

    def remove_enum(self, name: str) -> pb_enum.Enum:
        map_enums = self.map_enums
        enum = None
        if name in map_enums:
            enum = map_enums[name]
            self.arr_enums.remove(enum)
            del map_enums[name]
        return enum

    def add_message(self, name: str, option: dict = None) -> pb_message.Message:
        self.remove_message(name)
        message = pb_message.Message(name, option)
        self.arr_messages.append(message)
        self.map_messages[name] = message
        return message

    def remove_message(self, name: str) -> pb_message.Message:
        map_messages = self.map_messages
        message = None
        if name in map_messages:
            message = map_messages[name]
            self.arr_messages.remove(message)
            del map_messages[name]
        return message
