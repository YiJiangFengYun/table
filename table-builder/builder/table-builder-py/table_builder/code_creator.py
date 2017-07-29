from enum import Enum
from typing import List
from os import path
import subprocess
import os


class ECodeTypes(Enum):
    PYTHON = 0
    COUNT = 1


class CodeCreator:
    def __init__(self, output_dir: str, protoc_path: str):
        self.protoc_path = protoc_path
        self.output_dir = output_dir
        self.temp_proto_file_name = "temp.proto"

    def create(self, doc_text: str, types: List[ECodeTypes] = None):
        if types is None:
            types = []
            for code_type in range(ECodeTypes.COUNT):
                types.append(code_type)
        if len(doc_text) > 0:
            # Create temp .proto file
            temp_file_path = path.join(self.output_dir, self.temp_proto_file_name)
            file = open(temp_file_path, "w")
            file.write(doc_text)
            file.close()

            #  Call protoc command to create code
            for code_type in types:
                if code_type == ECodeTypes.PYTHON:
                    self._create_python(temp_file_path)
                else:
                    raise ValueError("Type is undefined.")

            # Delete temp .proto file
            os.remove(temp_file_path)

    def _create_python(self, proto_file_path: str):
        subprocess.call([path.join(self.protoc_path, "protoc"),
                         "--proto_path=" + self.output_dir,
                         "--python_out=" + self.output_dir,
                         self.temp_proto_file_name])
