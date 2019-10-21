# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/submit_combat_challenge_pokemons_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_challenge_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/submit_combat_challenge_pokemons_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nOpogoprotos/networking/responses/submit_combat_challenge_pokemons_response.proto\x12\x1fpogoprotos.networking.responses\x1a-pogoprotos/data/combat/combat_challenge.proto\"\xd8\x03\n%SubmitCombatChallengePokemonsResponse\x12]\n\x06result\x18\x01 \x01(\x0e\x32M.pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse.Result\x12:\n\tchallenge\x18\x02 \x01(\x0b\x32\'.pogoprotos.data.combat.CombatChallenge\"\x93\x02\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12!\n\x1d\x45RROR_INVALID_CHALLENGE_STATE\x10\x02\x12\x1d\n\x19\x45RROR_CHALLENGE_NOT_FOUND\x10\x03\x12\"\n\x1e\x45RROR_POKEMON_NOT_IN_INVENTORY\x10\x04\x12\x1d\n\x19\x45RROR_NOT_ELIGIBLE_LEAGUE\x10\x05\x12\x1a\n\x16\x45RROR_ALREADY_TIMEDOUT\x10\x06\x12\x1b\n\x17\x45RROR_ALREADY_CANCELLED\x10\x07\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x08\x12\x1a\n\x16\x45RROR_ALREADY_DECLINED\x10\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2.DESCRIPTOR,])



_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_CHALLENGE_STATE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CHALLENGE_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_IN_INVENTORY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_ELIGIBLE_LEAGUE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_TIMEDOUT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_CANCELLED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_DECLINED', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=361,
  serialized_end=636,
)
_sym_db.RegisterEnumDescriptor(_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE_RESULT)


_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE = _descriptor.Descriptor(
  name='SubmitCombatChallengePokemonsResponse',
  full_name='pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge', full_name='pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse.challenge', index=1,
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
    _SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=636,
)

_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE.fields_by_name['result'].enum_type = _SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE_RESULT
_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE.fields_by_name['challenge'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__challenge__pb2._COMBATCHALLENGE
_SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE_RESULT.containing_type = _SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE
DESCRIPTOR.message_types_by_name['SubmitCombatChallengePokemonsResponse'] = _SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitCombatChallengePokemonsResponse = _reflection.GeneratedProtocolMessageType('SubmitCombatChallengePokemonsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITCOMBATCHALLENGEPOKEMONSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.submit_combat_challenge_pokemons_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.SubmitCombatChallengePokemonsResponse)
  ))
_sym_db.RegisterMessage(SubmitCombatChallengePokemonsResponse)


# @@protoc_insertion_point(module_scope)
