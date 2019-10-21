# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/badge/gym_badge_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.gym import gym_battle_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__battle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/badge/gym_badge_stats.proto',
  package='pogoprotos.data.badge',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+pogoprotos/data/badge/gym_badge_stats.proto\x12\x15pogoprotos.data.badge\x1a$pogoprotos/data/gym/gym_battle.proto\"\xc5\x01\n\rGymBadgeStats\x12\x1e\n\x16total_time_defended_ms\x18\x01 \x01(\x04\x12\x17\n\x0fnum_battles_won\x18\x02 \x01(\r\x12\x18\n\x10num_battles_lost\x18\x05 \x01(\r\x12\x17\n\x0fnum_berries_fed\x18\x03 \x01(\r\x12\x13\n\x0bnum_deploys\x18\x04 \x01(\r\x12\x33\n\x0bgym_battles\x18\x0f \x03(\x0b\x32\x1e.pogoprotos.data.gym.GymBattleb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_gym_dot_gym__battle__pb2.DESCRIPTOR,])




_GYMBADGESTATS = _descriptor.Descriptor(
  name='GymBadgeStats',
  full_name='pogoprotos.data.badge.GymBadgeStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_time_defended_ms', full_name='pogoprotos.data.badge.GymBadgeStats.total_time_defended_ms', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_battles_won', full_name='pogoprotos.data.badge.GymBadgeStats.num_battles_won', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_battles_lost', full_name='pogoprotos.data.badge.GymBadgeStats.num_battles_lost', index=2,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_berries_fed', full_name='pogoprotos.data.badge.GymBadgeStats.num_berries_fed', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_deploys', full_name='pogoprotos.data.badge.GymBadgeStats.num_deploys', index=4,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gym_battles', full_name='pogoprotos.data.badge.GymBadgeStats.gym_battles', index=5,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=306,
)

_GYMBADGESTATS.fields_by_name['gym_battles'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__battle__pb2._GYMBATTLE
DESCRIPTOR.message_types_by_name['GymBadgeStats'] = _GYMBADGESTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymBadgeStats = _reflection.GeneratedProtocolMessageType('GymBadgeStats', (_message.Message,), dict(
  DESCRIPTOR = _GYMBADGESTATS,
  __module__ = 'pogoprotos.data.badge.gym_badge_stats_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.badge.GymBadgeStats)
  ))
_sym_db.RegisterMessage(GymBadgeStats)


# @@protoc_insertion_point(module_scope)
