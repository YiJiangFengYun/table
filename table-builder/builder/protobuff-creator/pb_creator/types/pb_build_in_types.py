from pb_creator.types import pb_type
from typing import Dict
from typing import Mapping
from typing import Any

type_double = pb_type.Type("double")
type_float = pb_type.Type("float")
type_int32 = pb_type.Type("int32")
type_int64 = pb_type.Type("int64")
type_uint32 = pb_type.Type("uint32")
type_uint64 = pb_type.Type("uint64")
type_sint32 = pb_type.Type("sint32")
type_sint64 = pb_type.Type("sint64")
type_fixed32 = pb_type.Type("fixed32")
type_fixed64 = pb_type.Type("fixed64")
type_sfixed32 = pb_type.Type("sfixed32")
type_sfixed64 = pb_type.Type("sfixed64")
type_bool = pb_type.Type("bool")
type_string = pb_type.Type("string")
type_bytes = pb_type.Type("bytes")
type_any = pb_type.Type("google.protobuf.Any")

map_types: Dict[str, pb_type.Type] = {}


def __construct_types(types: Dict[str, pb_type.Type], local_scopes: Mapping[str, Any]):
    for key, variable in local_scopes.items():
        if isinstance(variable, pb_type.Type):
            var_type: pb_type.Type = variable
            types[var_type.name] = var_type


__construct_types(map_types, locals())
