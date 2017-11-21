import importlib
import pathlib
import subprocess
import sys
import typing
from enum import Enum

from pb_creator import pb_document


class ECodeTypes(Enum):
    PYTHON = 0
    CPP = 1
    CSharp = 2
    JS = 3
    COUNT = 4


class CodeCreator:
    def __init__(self,
                 output_dir: pathlib.Path,
                 protoc_path: pathlib.Path,
                 table_locals: typing.Dict[str, typing.Any]):
        self.protoc_path: pathlib.Path = protoc_path
        self.output_dir: pathlib.Path = output_dir
        self.table_locals = table_locals

    def create(self, doc: pb_document.Document):
        python_module_name: str = None
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
                    python_module_name = self._create_python(doc_name, proto_file_name, self.output_dir)
                elif code_type == ECodeTypes.CPP:
                    self._create_cpp(doc_name, proto_file_name, self.output_dir)
                elif code_type == ECodeTypes.CSharp:
                    self._create_csharp(doc_name, proto_file_name, self.output_dir)
                elif code_type == ECodeTypes.JS:
                    self._create_js(doc_name, proto_file_name, self.output_dir)
                else:
                    raise ValueError("Type is undefined.")

                    # # Delete .proto file
                    # os.remove(str(temp_file_path))
        if python_module_name is None:
            raise RuntimeError("Create python module name error.")
        return python_module_name

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
        if python_out_path not in sys.path:
            sys.path.append(str(python_out_path))
        python_module_name = doc_name + "_pb2"
        result = importlib.import_module(python_module_name)
        self.table_locals[python_module_name] = result
        return python_module_name

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

    def _create_js(self, doc_name: str, proto_file_name: str, output_dir: pathlib.Path):
        js_out_path = output_dir.joinpath("js")
        js_out_path.mkdir(exist_ok=True)
        subprocess.run([str(self.protoc_path),
                        "--proto_path=" + str(output_dir),
                        "--js_out=" + str(js_out_path),
                        str(output_dir.joinpath(proto_file_name))])
