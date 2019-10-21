# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/combat_friend_request_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/combat_friend_request_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/responses/combat_friend_request_response.proto\x12\x1fpogoprotos.networking.responses\"\x84\x02\n\x1b\x43ombatFriendRequestResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.responses.CombatFriendRequestResponse.Result\"\x8f\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_COMBAT_NOT_FOUND\x10\x02\x12\x1b\n\x17\x45RROR_COMBAT_INCOMPLETE\x10\x03\x12\x1e\n\x1a\x45RROR_PLAYER_NOT_IN_COMBAT\x10\x04\x12\x14\n\x10\x45RROR_SOCIAL_RPC\x10\x05\x62\x06proto3')
)



_COMBATFRIENDREQUESTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.CombatFriendRequestResponse.Result',
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
      name='ERROR_COMBAT_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_COMBAT_INCOMPLETE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_IN_COMBAT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SOCIAL_RPC', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=223,
  serialized_end=366,
)
_sym_db.RegisterEnumDescriptor(_COMBATFRIENDREQUESTRESPONSE_RESULT)


_COMBATFRIENDREQUESTRESPONSE = _descriptor.Descriptor(
  name='CombatFriendRequestResponse',
  full_name='pogoprotos.networking.responses.CombatFriendRequestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CombatFriendRequestResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMBATFRIENDREQUESTRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=366,
)

_COMBATFRIENDREQUESTRESPONSE.fields_by_name['result'].enum_type = _COMBATFRIENDREQUESTRESPONSE_RESULT
_COMBATFRIENDREQUESTRESPONSE_RESULT.containing_type = _COMBATFRIENDREQUESTRESPONSE
DESCRIPTOR.message_types_by_name['CombatFriendRequestResponse'] = _COMBATFRIENDREQUESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatFriendRequestResponse = _reflection.GeneratedProtocolMessageType('CombatFriendRequestResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMBATFRIENDREQUESTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.combat_friend_request_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CombatFriendRequestResponse)
  ))
_sym_db.RegisterMessage(CombatFriendRequestResponse)


# @@protoc_insertion_point(module_scope)
