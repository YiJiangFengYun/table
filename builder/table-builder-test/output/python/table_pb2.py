# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: table.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='table.proto',
  package='table',
  syntax='proto3',
  serialized_pb=_b('\n\x0btable.proto\x12\x05table\x1a\x19google/protobuf/any.proto\"*\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\">\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\ttype_name\x18\x03 \x01(\t\"1\n\x07Wrapper\x12&\n\x08\x63ontents\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='table.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='table.Table.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='table.Table.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=91,
)


_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='table.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='table.Column.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='table.Column.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_name', full_name='table.Column.type_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=155,
)


_WRAPPER = _descriptor.Descriptor(
  name='Wrapper',
  full_name='table.Wrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='table.Wrapper.contents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=206,
)

_WRAPPER.fields_by_name['contents'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['Column'] = _COLUMN
DESCRIPTOR.message_types_by_name['Wrapper'] = _WRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), dict(
  DESCRIPTOR = _TABLE,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.Table)
  ))
_sym_db.RegisterMessage(Table)

Column = _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), dict(
  DESCRIPTOR = _COLUMN,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.Column)
  ))
_sym_db.RegisterMessage(Column)

Wrapper = _reflection.GeneratedProtocolMessageType('Wrapper', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPER,
  __module__ = 'table_pb2'
  # @@protoc_insertion_point(class_scope:table.Wrapper)
  ))
_sym_db.RegisterMessage(Wrapper)


# @@protoc_insertion_point(module_scope)
