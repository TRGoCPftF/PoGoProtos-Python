# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/list_gym_badges_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/list_gym_badges_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEpogoprotos/networking/requests/messages/list_gym_badges_message.proto\x12\'pogoprotos.networking.requests.messages\"\x16\n\x14ListGymBadgesMessageb\x06proto3')
)




_LISTGYMBADGESMESSAGE = _descriptor.Descriptor(
  name='ListGymBadgesMessage',
  full_name='pogoprotos.networking.requests.messages.ListGymBadgesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=114,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['ListGymBadgesMessage'] = _LISTGYMBADGESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListGymBadgesMessage = _reflection.GeneratedProtocolMessageType('ListGymBadgesMessage', (_message.Message,), dict(
  DESCRIPTOR = _LISTGYMBADGESMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.list_gym_badges_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.ListGymBadgesMessage)
  ))
_sym_db.RegisterMessage(ListGymBadgesMessage)


# @@protoc_insertion_point(module_scope)
