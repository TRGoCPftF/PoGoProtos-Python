# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_camera.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_camera.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/data/player/player_camera.proto\x12\x16pogoprotos.data.player\")\n\x0cPlayerCamera\x12\x19\n\x11is_default_camera\x18\x01 \x01(\x08\x62\x06proto3')
)




_PLAYERCAMERA = _descriptor.Descriptor(
  name='PlayerCamera',
  full_name='pogoprotos.data.player.PlayerCamera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_default_camera', full_name='pogoprotos.data.player.PlayerCamera.is_default_camera', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=70,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['PlayerCamera'] = _PLAYERCAMERA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerCamera = _reflection.GeneratedProtocolMessageType('PlayerCamera', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERCAMERA,
  __module__ = 'pogoprotos.data.player.player_camera_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerCamera)
  ))
_sym_db.RegisterMessage(PlayerCamera)


# @@protoc_insertion_point(module_scope)
