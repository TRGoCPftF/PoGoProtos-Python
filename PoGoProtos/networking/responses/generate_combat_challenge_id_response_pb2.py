# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/generate_combat_challenge_id_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/generate_combat_challenge_id_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nKpogoprotos/networking/responses/generate_combat_challenge_id_response.proto\x12\x1fpogoprotos.networking.responses\"\xf5\x01\n!GenerateCombatChallengeIdResponse\x12Y\n\x06result\x18\x01 \x01(\x0e\x32I.pogoprotos.networking.responses.GenerateCombatChallengeIdResponse.Result\x12\x14\n\x0c\x63hallenge_id\x18\x02 \x01(\t\"_\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x02\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x03\x62\x06proto3')
)



_GENERATECOMBATCHALLENGEIDRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GenerateCombatChallengeIdResponse.Result',
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
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=263,
  serialized_end=358,
)
_sym_db.RegisterEnumDescriptor(_GENERATECOMBATCHALLENGEIDRESPONSE_RESULT)


_GENERATECOMBATCHALLENGEIDRESPONSE = _descriptor.Descriptor(
  name='GenerateCombatChallengeIdResponse',
  full_name='pogoprotos.networking.responses.GenerateCombatChallengeIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GenerateCombatChallengeIdResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_id', full_name='pogoprotos.networking.responses.GenerateCombatChallengeIdResponse.challenge_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GENERATECOMBATCHALLENGEIDRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=358,
)

_GENERATECOMBATCHALLENGEIDRESPONSE.fields_by_name['result'].enum_type = _GENERATECOMBATCHALLENGEIDRESPONSE_RESULT
_GENERATECOMBATCHALLENGEIDRESPONSE_RESULT.containing_type = _GENERATECOMBATCHALLENGEIDRESPONSE
DESCRIPTOR.message_types_by_name['GenerateCombatChallengeIdResponse'] = _GENERATECOMBATCHALLENGEIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateCombatChallengeIdResponse = _reflection.GeneratedProtocolMessageType('GenerateCombatChallengeIdResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERATECOMBATCHALLENGEIDRESPONSE,
  __module__ = 'pogoprotos.networking.responses.generate_combat_challenge_id_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GenerateCombatChallengeIdResponse)
  ))
_sym_db.RegisterMessage(GenerateCombatChallengeIdResponse)


# @@protoc_insertion_point(module_scope)
