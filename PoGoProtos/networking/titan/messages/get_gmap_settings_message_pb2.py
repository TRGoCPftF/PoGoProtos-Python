# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/titan/messages/get_gmap_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/titan/messages/get_gmap_settings_message.proto',
  package='pogoprotos.networking.titan.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/titan/messages/get_gmap_settings_message.proto\x12$pogoprotos.networking.titan.messages\"\x18\n\x16GetGmapSettingsMessageb\x06proto3')
)




_GETGMAPSETTINGSMESSAGE = _descriptor.Descriptor(
  name='GetGmapSettingsMessage',
  full_name='pogoprotos.networking.titan.messages.GetGmapSettingsMessage',
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
  serialized_start=110,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['GetGmapSettingsMessage'] = _GETGMAPSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGmapSettingsMessage = _reflection.GeneratedProtocolMessageType('GetGmapSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETGMAPSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.titan.messages.get_gmap_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.titan.messages.GetGmapSettingsMessage)
  ))
_sym_db.RegisterMessage(GetGmapSettingsMessage)


# @@protoc_insertion_point(module_scope)
