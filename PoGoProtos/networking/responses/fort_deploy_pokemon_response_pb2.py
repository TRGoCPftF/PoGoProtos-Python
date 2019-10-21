# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/fort_deploy_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.gym import gym_state_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__state__pb2
from pogoprotos.networking.responses import fort_details_response_pb2 as pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/fort_deploy_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBpogoprotos/networking/responses/fort_deploy_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\x1a#pogoprotos/data/gym/gym_state.proto\x1a;pogoprotos/networking/responses/fort_details_response.proto\"\xd9\x05\n\x19\x46ortDeployPokemonResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.FortDeployPokemonResponse.Result\x12J\n\x0c\x66ort_details\x18\x02 \x01(\x0b\x32\x34.pogoprotos.networking.responses.FortDetailsResponse\x12\x32\n\x0cpokemon_data\x18\x03 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x30\n\tgym_state\x18\x04 \x01(\x0b\x32\x1d.pogoprotos.data.gym.GymState\"\xb6\x03\n\x06Result\x12\x11\n\rNO_RESULT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12%\n!ERROR_ALREADY_HAS_POKEMON_ON_FORT\x10\x02\x12!\n\x1d\x45RROR_OPPOSING_TEAM_OWNS_FORT\x10\x03\x12\x16\n\x12\x45RROR_FORT_IS_FULL\x10\x04\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x05\x12\x1c\n\x18\x45RROR_PLAYER_HAS_NO_TEAM\x10\x06\x12\x1d\n\x19\x45RROR_POKEMON_NOT_FULL_HP\x10\x07\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x08\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\t\x12\x1d\n\x19\x45RROR_FORT_DEPLOY_LOCKOUT\x10\n\x12 \n\x1c\x45RROR_PLAYER_HAS_NO_NICKNAME\x10\x0b\x12\x1a\n\x16\x45RROR_POI_INACCESSIBLE\x10\x0c\x12\x1b\n\x17\x45RROR_LEGENDARY_POKEMON\x10\r\x12\x19\n\x15\x45RROR_INVALID_POKEMON\x10\x0e\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_gym_dot_gym__state__pb2.DESCRIPTOR,pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2.DESCRIPTOR,])



_FORTDEPLOYPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.FortDeployPokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_RESULT_SET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_HAS_POKEMON_ON_FORT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_OPPOSING_TEAM_OWNS_FORT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_IS_FULL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_TEAM', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_FULL_HP', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FORT_DEPLOY_LOCKOUT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_NICKNAME', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POI_INACCESSIBLE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_LEGENDARY_POKEMON', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_POKEMON', index=14, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=529,
  serialized_end=967,
)
_sym_db.RegisterEnumDescriptor(_FORTDEPLOYPOKEMONRESPONSE_RESULT)


_FORTDEPLOYPOKEMONRESPONSE = _descriptor.Descriptor(
  name='FortDeployPokemonResponse',
  full_name='pogoprotos.networking.responses.FortDeployPokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.FortDeployPokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fort_details', full_name='pogoprotos.networking.responses.FortDeployPokemonResponse.fort_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='pogoprotos.networking.responses.FortDeployPokemonResponse.pokemon_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_state', full_name='pogoprotos.networking.responses.FortDeployPokemonResponse.gym_state', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FORTDEPLOYPOKEMONRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=967,
)

_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['result'].enum_type = _FORTDEPLOYPOKEMONRESPONSE_RESULT
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['fort_details'].message_type = pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2._FORTDETAILSRESPONSE
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_FORTDEPLOYPOKEMONRESPONSE.fields_by_name['gym_state'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__state__pb2._GYMSTATE
_FORTDEPLOYPOKEMONRESPONSE_RESULT.containing_type = _FORTDEPLOYPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['FortDeployPokemonResponse'] = _FORTDEPLOYPOKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortDeployPokemonResponse = _reflection.GeneratedProtocolMessageType('FortDeployPokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORTDEPLOYPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.fort_deploy_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.FortDeployPokemonResponse)
  ))
_sym_db.RegisterMessage(FortDeployPokemonResponse)


# @@protoc_insertion_point(module_scope)
