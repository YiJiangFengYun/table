from pathlib import Path

from table_builder import builder

output: Path = Path("./output")
output.mkdir(exist_ok=True)
table_builder = builder.Builder(pb_version=3,
                                excels_dir=Path("."),
                                code_output_dir=output,
                                binary_output_dir=output,
                                protoc_path=Path("./protoc-3.3.0-win32/bin/protoc.exe"))
table_builder.build()
