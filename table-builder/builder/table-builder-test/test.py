from table_builder import builder

table_builder = builder.Builder(3, ".", "./output", ".", "./protoc-3.3.0-win32/bin/protoc.exe")
table_builder.build()

