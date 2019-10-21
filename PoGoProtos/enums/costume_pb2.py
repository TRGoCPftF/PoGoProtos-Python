# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/costume.proto

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
  name='pogoprotos/enums/costume.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1epogoprotos/enums/costume.proto\x12\x10pogoprotos.enums*\xd6\x01\n\x07\x43ostume\x12\x11\n\rCOSTUME_UNSET\x10\x00\x12\x10\n\x0cHOLIDAY_2016\x10\x01\x12\x0f\n\x0b\x41NNIVERSARY\x10\x02\x12\x18\n\x14ONE_YEAR_ANNIVERSARY\x10\x03\x12\x12\n\x0eHALLOWEEN_2017\x10\x04\x12\x0f\n\x0bSUMMER_2018\x10\x05\x12\r\n\tFALL_2018\x10\x06\x12\x11\n\rNOVEMBER_2018\x10\x07\x12\x0f\n\x0bWINTER_2018\x10\x08\x12\x0c\n\x08\x46\x45\x42_2019\x10\t\x12\x15\n\x11MAY_2019_NOEVOLVE\x10\nb\x06proto3')
)

_COSTUME = _descriptor.EnumDescriptor(
  name='Costume',
  full_name='pogoprotos.enums.Costume',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COSTUME_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLIDAY_2016', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNIVERSARY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_YEAR_ANNIVERSARY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALLOWEEN_2017', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUMMER_2018', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALL_2018', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOVEMBER_2018', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINTER_2018', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEB_2019', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAY_2019_NOEVOLVE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=53,
  serialized_end=267,
)
_sym_db.RegisterEnumDescriptor(_COSTUME)

Costume = enum_type_wrapper.EnumTypeWrapper(_COSTUME)
COSTUME_UNSET = 0
HOLIDAY_2016 = 1
ANNIVERSARY = 2
ONE_YEAR_ANNIVERSARY = 3
HALLOWEEN_2017 = 4
SUMMER_2018 = 5
FALL_2018 = 6
NOVEMBER_2018 = 7
WINTER_2018 = 8
FEB_2019 = 9
MAY_2019_NOEVOLVE = 10


DESCRIPTOR.enum_types_by_name['Costume'] = _COSTUME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
