# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/gym_deploy_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/gym_deploy_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/networking/requests/messages/gym_deploy_message.proto\x12\'pogoprotos.networking.requests.messages\"j\n\x10GymDeployMessage\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x12\n\npokemon_id\x18\x02 \x01(\x06\x12\x17\n\x0fplayer_latitude\x18\x03 \x01(\x01\x12\x18\n\x10player_longitude\x18\x04 \x01(\x01\x62\x06proto3')
)




_GYMDEPLOYMESSAGE = _descriptor.Descriptor(
  name='GymDeployMessage',
  full_name='pogoprotos.networking.requests.messages.GymDeployMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.requests.messages.GymDeployMessage.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.requests.messages.GymDeployMessage.pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='pogoprotos.networking.requests.messages.GymDeployMessage.player_latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='pogoprotos.networking.requests.messages.GymDeployMessage.player_longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_end=215,
)

DESCRIPTOR.message_types_by_name['GymDeployMessage'] = _GYMDEPLOYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymDeployMessage = _reflection.GeneratedProtocolMessageType('GymDeployMessage', (_message.Message,), dict(
  DESCRIPTOR = _GYMDEPLOYMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.gym_deploy_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GymDeployMessage)
  ))
_sym_db.RegisterMessage(GymDeployMessage)


# @@protoc_insertion_point(module_scope)
