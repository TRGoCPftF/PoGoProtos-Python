# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_create_context.proto

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
  name='pogoprotos/enums/pokemon_create_context.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/enums/pokemon_create_context.proto\x12\x10pogoprotos.enums*b\n\x14PokemonCreateContext\x12\x17\n\x13\x43REATE_CONTEXT_WILD\x10\x00\x12\x16\n\x12\x43REATE_CONTEXT_EGG\x10\x01\x12\x19\n\x15\x43REATE_CONTEXT_EVOLVE\x10\x02\x62\x06proto3')
)

_POKEMONCREATECONTEXT = _descriptor.EnumDescriptor(
  name='PokemonCreateContext',
  full_name='pogoprotos.enums.PokemonCreateContext',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE_CONTEXT_WILD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_CONTEXT_EGG', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_CONTEXT_EVOLVE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=67,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_POKEMONCREATECONTEXT)

PokemonCreateContext = enum_type_wrapper.EnumTypeWrapper(_POKEMONCREATECONTEXT)
CREATE_CONTEXT_WILD = 0
CREATE_CONTEXT_EGG = 1
CREATE_CONTEXT_EVOLVE = 2


DESCRIPTOR.enum_types_by_name['PokemonCreateContext'] = _POKEMONCREATECONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
