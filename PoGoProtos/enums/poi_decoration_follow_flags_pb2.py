# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/poi_decoration_follow_flags.proto

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
  name='pogoprotos/enums/poi_decoration_follow_flags.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2pogoprotos/enums/poi_decoration_follow_flags.proto\x12\x10pogoprotos.enums*o\n\x18POIDecorationFollowFlags\x12)\n%POIDECORATIONFOLLOWFLAGS_AUTO_INVALID\x10\x00\x12\x0c\n\x08\x46OLLOW_X\x10\x01\x12\x0c\n\x08\x46OLLOW_Y\x10\x02\x12\x0c\n\x08\x46OLLOW_Z\x10\x04\x62\x06proto3')
)

_POIDECORATIONFOLLOWFLAGS = _descriptor.EnumDescriptor(
  name='POIDecorationFollowFlags',
  full_name='pogoprotos.enums.POIDecorationFollowFlags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POIDECORATIONFOLLOWFLAGS_AUTO_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW_X', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW_Y', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW_Z', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=72,
  serialized_end=183,
)
_sym_db.RegisterEnumDescriptor(_POIDECORATIONFOLLOWFLAGS)

POIDecorationFollowFlags = enum_type_wrapper.EnumTypeWrapper(_POIDECORATIONFOLLOWFLAGS)
POIDECORATIONFOLLOWFLAGS_AUTO_INVALID = 0
FOLLOW_X = 1
FOLLOW_Y = 2
FOLLOW_Z = 4


DESCRIPTOR.enum_types_by_name['POIDecorationFollowFlags'] = _POIDECORATIONFOLLOWFLAGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
