# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gym/gym_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import fort_data_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__data__pb2
from pogoprotos.data.gym import gym_membership_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__membership__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/gym/gym_state.proto',
  package='pogoprotos.data.gym',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#pogoprotos/data/gym/gym_state.proto\x12\x13pogoprotos.data.gym\x1a#pogoprotos/map/fort/fort_data.proto\x1a(pogoprotos/data/gym/gym_membership.proto\"\x8d\x01\n\x08GymState\x12\x30\n\tfort_data\x18\x01 \x01(\x0b\x32\x1d.pogoprotos.map.fort.FortData\x12\x37\n\x0bmemberships\x18\x02 \x03(\x0b\x32\".pogoprotos.data.gym.GymMembership\x12\x16\n\x0e\x64\x65ploy_lockout\x18\x03 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_fort__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_gym_dot_gym__membership__pb2.DESCRIPTOR,])




_GYMSTATE = _descriptor.Descriptor(
  name='GymState',
  full_name='pogoprotos.data.gym.GymState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_data', full_name='pogoprotos.data.gym.GymState.fort_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memberships', full_name='pogoprotos.data.gym.GymState.memberships', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploy_lockout', full_name='pogoprotos.data.gym.GymState.deploy_lockout', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=140,
  serialized_end=281,
)

_GYMSTATE.fields_by_name['fort_data'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__data__pb2._FORTDATA
_GYMSTATE.fields_by_name['memberships'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__membership__pb2._GYMMEMBERSHIP
DESCRIPTOR.message_types_by_name['GymState'] = _GYMSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymState = _reflection.GeneratedProtocolMessageType('GymState', (_message.Message,), dict(
  DESCRIPTOR = _GYMSTATE,
  __module__ = 'pogoprotos.data.gym.gym_state_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.gym.GymState)
  ))
_sym_db.RegisterMessage(GymState)


# @@protoc_insertion_point(module_scope)
