import os
import pathlib
import subprocess
from enum import Enum

from pb_creator import pb_document


class ECodeTypes(Enum):
    PYTHON = 0
    COUNT = 1


class CodeCreator:
    def __init__(self, output_dir: str, protoc_path: str):
        self.protoc_path: pathlib.Path = pathlib.Path(protoc_path)
        self.output_dir: pathlib.Path = pathlib.Path(output_dir)

    def create(self, doc: pb_document.Document):
        types = []
        for code_type in range(ECodeTypes.COUNT.value):
            types.append(ECodeTypes(code_type))
        doc_text = doc.to_text()
        if len(doc_text) > 0:
            # Create temp .proto file
            proto_file_name = doc.name + ".proto"
            temp_file_path: pathlib.Path = self.output_dir.joinpath(proto_file_name)
            file = open(temp_file_path, "w")
            file.write(doc_text)
            file.close()

            #  Call protoc command to create code
            for code_type in types:
                if code_type == ECodeTypes.PYTHON:
                    self._create_python(proto_file_name)
                else:
                    raise ValueError("Type is undefined.")

            # Delete temp .proto file
            os.remove(str(temp_file_path))

    def _create_python(self, proto_file_name: str):
        python_out_path = self.output_dir.joinpath("python")
        python_out_path.mkdir(exist_ok=True)
        subprocess.run([str(self.protoc_path),
                        "--proto_path=" + str(self.output_dir),
                        "--python_out=" + str(python_out_path),
                        str(self.output_dir.joinpath(proto_file_name))])
