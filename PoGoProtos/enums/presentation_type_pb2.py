# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/presentation_type.proto

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
  name='pogoprotos/enums/presentation_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/enums/presentation_type.proto\x12\x10pogoprotos.enums*S\n\x10PresentationType\x12\x1d\n\x19UNKNOWN_PRESENTATION_TYPE\x10\x00\x12\x0c\n\x08\x43\x41TEGORY\x10\x01\x12\x08\n\x04SORT\x10\x02\x12\x08\n\x04SALE\x10\x03\x62\x06proto3')
)

_PRESENTATIONTYPE = _descriptor.EnumDescriptor(
  name='PresentationType',
  full_name='pogoprotos.enums.PresentationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PRESENTATION_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SORT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=145,
)
_sym_db.RegisterEnumDescriptor(_PRESENTATIONTYPE)

PresentationType = enum_type_wrapper.EnumTypeWrapper(_PRESENTATIONTYPE)
UNKNOWN_PRESENTATION_TYPE = 0
CATEGORY = 1
SORT = 2
SALE = 3


DESCRIPTOR.enum_types_by_name['PresentationType'] = _PRESENTATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)