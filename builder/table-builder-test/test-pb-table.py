from output.python import table_pb2

table_test = table_pb2.Table()
# #  Assign a integer to name
# table_test.name = 1

# #  Assgin a integer to attribute not defined
# table_test.color = 1

#  Assign a string to name
print(type(getattr(table_test, "name")))
table_test.name = type(getattr(table_test, "name"))(1)
print("table_test.name: {}".format(table_test.name))
setattr(table_test, "name", "test_table")
