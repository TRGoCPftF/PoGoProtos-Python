# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/gym_battle_attack_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_update_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__update__pb2
from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/gym_battle_attack_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/responses/gym_battle_attack_response.proto\x12\x1fpogoprotos.networking.responses\x1a*pogoprotos/data/battle/battle_update.proto\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\"\xf3\x02\n\x17GymBattleAttackResponse\x12O\n\x06result\x18\x01 \x01(\x0e\x32?.pogoprotos.networking.responses.GymBattleAttackResponse.Result\x12;\n\rbattle_update\x18\x02 \x01(\x0b\x32$.pogoprotos.data.battle.BattleUpdate\x12\x39\n\tgym_badge\x18\x03 \x01(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\"\x8e\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12 \n\x1c\x45RROR_INVALID_ATTACK_ACTIONS\x10\x02\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x03\x12\x1b\n\x17\x45RROR_WRONG_BATTLE_TYPE\x10\x04\x12\x15\n\x11\x45RROR_RAID_ACTIVE\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__update__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,])



_GYMBATTLEATTACKRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GymBattleAttackResponse.Result',
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
      name='ERROR_INVALID_ATTACK_ACTIONS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_WRONG_BATTLE_TYPE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RAID_ACTIVE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=422,
  serialized_end=564,
)
_sym_db.RegisterEnumDescriptor(_GYMBATTLEATTACKRESPONSE_RESULT)


_GYMBATTLEATTACKRESPONSE = _descriptor.Descriptor(
  name='GymBattleAttackResponse',
  full_name='pogoprotos.networking.responses.GymBattleAttackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GymBattleAttackResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battle_update', full_name='pogoprotos.networking.responses.GymBattleAttackResponse.battle_update', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_badge', full_name='pogoprotos.networking.responses.GymBattleAttackResponse.gym_badge', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GYMBATTLEATTACKRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=564,
)

_GYMBATTLEATTACKRESPONSE.fields_by_name['result'].enum_type = _GYMBATTLEATTACKRESPONSE_RESULT
_GYMBATTLEATTACKRESPONSE.fields_by_name['battle_update'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__update__pb2._BATTLEUPDATE
_GYMBATTLEATTACKRESPONSE.fields_by_name['gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GYMBATTLEATTACKRESPONSE_RESULT.containing_type = _GYMBATTLEATTACKRESPONSE
DESCRIPTOR.message_types_by_name['GymBattleAttackResponse'] = _GYMBATTLEATTACKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymBattleAttackResponse = _reflection.GeneratedProtocolMessageType('GymBattleAttackResponse', (_message.Message,), dict(
  DESCRIPTOR = _GYMBATTLEATTACKRESPONSE,
  __module__ = 'pogoprotos.networking.responses.gym_battle_attack_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GymBattleAttackResponse)
  ))
_sym_db.RegisterMessage(GymBattleAttackResponse)


# @@protoc_insertion_point(module_scope)
