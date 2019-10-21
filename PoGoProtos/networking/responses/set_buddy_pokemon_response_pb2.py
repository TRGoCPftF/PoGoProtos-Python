# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/set_buddy_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import buddy_pokemon_pb2 as pogoprotos_dot_data_dot_buddy__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/set_buddy_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/responses/set_buddy_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a#pogoprotos/data/buddy_pokemon.proto\"\xb1\x02\n\x17SetBuddyPokemonResponse\x12O\n\x06result\x18\x01 \x01(\x0e\x32?.pogoprotos.networking.responses.SetBuddyPokemonResponse.Result\x12\x34\n\rupdated_buddy\x18\x02 \x01(\x0b\x32\x1d.pogoprotos.data.BuddyPokemon\"\x8e\x01\n\x06Result\x12\t\n\x05UNEST\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_POKEMON_DEPLOYED\x10\x02\x12\x1b\n\x17\x45RROR_POKEMON_NOT_OWNED\x10\x03\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x04\x12\x19\n\x15\x45RROR_INVALID_POKEMON\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_buddy__pokemon__pb2.DESCRIPTOR,])



_SETBUDDYPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SetBuddyPokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNEST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_DEPLOYED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_OWNED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_EGG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_POKEMON', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=302,
  serialized_end=444,
)
_sym_db.RegisterEnumDescriptor(_SETBUDDYPOKEMONRESPONSE_RESULT)


_SETBUDDYPOKEMONRESPONSE = _descriptor.Descriptor(
  name='SetBuddyPokemonResponse',
  full_name='pogoprotos.networking.responses.SetBuddyPokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SetBuddyPokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_buddy', full_name='pogoprotos.networking.responses.SetBuddyPokemonResponse.updated_buddy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETBUDDYPOKEMONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=444,
)

_SETBUDDYPOKEMONRESPONSE.fields_by_name['result'].enum_type = _SETBUDDYPOKEMONRESPONSE_RESULT
_SETBUDDYPOKEMONRESPONSE.fields_by_name['updated_buddy'].message_type = pogoprotos_dot_data_dot_buddy__pokemon__pb2._BUDDYPOKEMON
_SETBUDDYPOKEMONRESPONSE_RESULT.containing_type = _SETBUDDYPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['SetBuddyPokemonResponse'] = _SETBUDDYPOKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetBuddyPokemonResponse = _reflection.GeneratedProtocolMessageType('SetBuddyPokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETBUDDYPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.set_buddy_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SetBuddyPokemonResponse)
  ))
_sym_db.RegisterMessage(SetBuddyPokemonResponse)


# @@protoc_insertion_point(module_scope)
