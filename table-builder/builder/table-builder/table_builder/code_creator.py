import os
import pathlib
import subprocess
import typing
from enum import Enum

from pb_creator import pb_document


class ECodeTypes(Enum):
    PYTHON = 0
    CPP = 1
    CSharp = 2
    COUNT = 4


class CodeCreator:
    def __init__(self,
                 output_dir: pathlib.Path,
                 protoc_path: pathlib.Path,
                 table_locals: typing.Mapping[str, typing.Any]):
        self.protoc_path: pathlib.Path = protoc_path
        self.output_dir: pathlib.Path = output_dir
        self.table_locals = table_locals

    def create(self, doc: pb_document.Document):
        types = []
        for code_type in range(ECodeTypes.COUNT.value):
            types.append(ECodeTypes(code_type))
        doc_text = doc.to_text()
        if len(doc_text) > 0:
            # Create temp .proto file
            doc_name = doc.name
            proto_file_name = doc.name + ".proto"
            temp_file_path: pathlib.Path = self.output_dir.joinpath(proto_file_name)
            file = open(temp_file_path, "w")
            file.write(doc_text)
            file.close()

            #  Call protoc command to create code
            for code_type in types:
                if code_type == ECodeTypes.PYTHON:
                    self._create_python(doc_name, proto_file_name, self.output_dir)
                elif code_type == ECodeTypes.CPP:
                    self._create_cpp(doc_name, proto_file_name, self.output_dir)
                elif code_type == ECodeTypes.CSharp:
                    self._create_csharp(doc_name, proto_file_name, self.output_dir)
                else:
                    raise ValueError("Type is undefined.")

            # Delete temp .proto file
            os.remove(str(temp_file_path))

    def _create_python(self, doc_name: str, proto_file_name: str, output_dir: pathlib.Path):
        python_out_path = output_dir.joinpath("python")
        python_out_path.mkdir(exist_ok=True)
        result = subprocess.run([str(self.protoc_path),
                                 "--proto_path=" + str(output_dir),
                                 "--python_out=" + str(python_out_path),
                                 str(output_dir.joinpath(proto_file_name))])
        result.check_returncode()
        # The process has finished.
        # load proto code and import it, because the runtime will use their definition.
        python_code_file_path = python_out_path.joinpath(doc_name + "_pb2.py")
        exec(open(python_code_file_path).read(), globals(), self.table_locals)

    def _create_cpp(self, doc_name: str, proto_file_name: str, output_dir: pathlib.Path):
        cpp_out_path = output_dir.joinpath("cpp")
        cpp_out_path.mkdir(exist_ok=True)
        subprocess.run([str(self.protoc_path),
                        "--proto_path=" + str(output_dir),
                        "--cpp_out=" + str(cpp_out_path),
                        str(output_dir.joinpath(proto_file_name))])

    def _create_csharp(self, doc_name: str, proto_file_name: str, output_dir: pathlib.Path):
        csharp_out_path = output_dir.joinpath("csharp")
        csharp_out_path.mkdir(exist_ok=True)
        subprocess.run([str(self.protoc_path),
                        "--proto_path=" + str(output_dir),
                        "--csharp_out=" + str(csharp_out_path),
                        str(output_dir.joinpath(proto_file_name))])