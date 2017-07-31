from pathlib import Path

from table_builder import builder

table_builder = builder.Builder(pb_version=3,
                                excels_dir=Path("."),
                                code_output_dir=Path("./output"),
                                binary_output_dir=Path("./output"),
                                protoc_path=Path("./protoc-3.3.0-win32/bin/protoc.exe"))
table_builder.build()
