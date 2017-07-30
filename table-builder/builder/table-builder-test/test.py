from pathlib import Path

from table_builder import builder

table_builder = builder.Builder(3, Path("."), Path("./output"), Path("."), Path("./protoc-3.3.0-win32/bin/protoc.exe"))
table_builder.build()
