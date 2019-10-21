# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_friendship_milestone_rewards_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_friendship_milestone_rewards_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nOpogoprotos/networking/responses/get_friendship_milestone_rewards_response.proto\x12\x1fpogoprotos.networking.responses\"\xba\x02\n%GetFriendshipMilestoneRewardsResponse\x12]\n\x06result\x18\x01 \x01(\x0e\x32M.pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse.Result\x12\x11\n\txp_reward\x18\x02 \x01(\x03\x12\x11\n\tfriend_id\x18\x03 \x01(\t\"\x8b\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x15\n\x11\x45RROR_NOT_FRIENDS\x10\x03\x12#\n\x1f\x45RROR_MILESTONE_ALREADY_AWARDED\x10\x04\x12\x1a\n\x16\x45RROR_FAILED_TO_UPDATE\x10\x05\x62\x06proto3')
)



_GETFRIENDSHIPMILESTONEREWARDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse.Result',
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
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_FRIENDS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MILESTONE_ALREADY_AWARDED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FAILED_TO_UPDATE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=292,
  serialized_end=431,
)
_sym_db.RegisterEnumDescriptor(_GETFRIENDSHIPMILESTONEREWARDSRESPONSE_RESULT)


_GETFRIENDSHIPMILESTONEREWARDSRESPONSE = _descriptor.Descriptor(
  name='GetFriendshipMilestoneRewardsResponse',
  full_name='pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_reward', full_name='pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse.xp_reward', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_id', full_name='pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse.friend_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETFRIENDSHIPMILESTONEREWARDSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=431,
)

_GETFRIENDSHIPMILESTONEREWARDSRESPONSE.fields_by_name['result'].enum_type = _GETFRIENDSHIPMILESTONEREWARDSRESPONSE_RESULT
_GETFRIENDSHIPMILESTONEREWARDSRESPONSE_RESULT.containing_type = _GETFRIENDSHIPMILESTONEREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['GetFriendshipMilestoneRewardsResponse'] = _GETFRIENDSHIPMILESTONEREWARDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFriendshipMilestoneRewardsResponse = _reflection.GeneratedProtocolMessageType('GetFriendshipMilestoneRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFRIENDSHIPMILESTONEREWARDSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_friendship_milestone_rewards_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetFriendshipMilestoneRewardsResponse)
  ))
_sym_db.RegisterMessage(GetFriendshipMilestoneRewardsResponse)


# @@protoc_insertion_point(module_scope)
