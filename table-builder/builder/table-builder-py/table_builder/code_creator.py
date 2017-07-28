from enum import Enum
from typing import List
from os import path
from subprocess import call


class ECodeTypes(Enum):
    PYTHON = 0
    COUNT = 1


class CodeCreator:
    def __init__(self, doc_text: str, output_dir: str, protoc_path: str):
        self.doc_text = doc_text
        self.protoc_path = protoc_path

    def create(self, types: List[ECodeTypes]):
        if len(self.doc_text) > 0:
            # Create temp .proto file
            temp_file_path = path.join(self, "temp.proto")
            file = open(temp_file_path, "w")
            file.write(self.doc_text)
            file.close()

            #  Call protoc command to create code
            for t in types:
                if t == ECodeTypes.PYTHON:
                    self._create_python(temp_file_path)
                else:
                    raise ValueError("Type is undefined.")

    def _create_python(self, proto_file_path: str):
        pass
