# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/fort_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/fort_type.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#pogoprotos/map/fort/fort_type.proto\x12\x13pogoprotos.map.fort*#\n\x08\x46ortType\x12\x07\n\x03GYM\x10\x00\x12\x0e\n\nCHECKPOINT\x10\x01\x62\x06proto3')
)

_FORTTYPE = _descriptor.EnumDescriptor(
  name='FortType',
  full_name='pogoprotos.map.fort.FortType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GYM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKPOINT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=95,
)
_sym_db.RegisterEnumDescriptor(_FORTTYPE)

FortType = enum_type_wrapper.EnumTypeWrapper(_FORTTYPE)
GYM = 0
CHECKPOINT = 1


DESCRIPTOR.enum_types_by_name['FortType'] = _FORTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
