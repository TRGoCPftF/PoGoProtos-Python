# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/get_client_telemetry_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/get_client_telemetry_settings_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nSpogoprotos/networking/platform/requests/get_client_telemetry_settings_message.proto\x12\'pogoprotos.networking.platform.requests\"#\n!GetClientTelemetrySettingsMessageb\x06proto3')
)




_GETCLIENTTELEMETRYSETTINGSMESSAGE = _descriptor.Descriptor(
  name='GetClientTelemetrySettingsMessage',
  full_name='pogoprotos.networking.platform.requests.GetClientTelemetrySettingsMessage',
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
  serialized_start=128,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['GetClientTelemetrySettingsMessage'] = _GETCLIENTTELEMETRYSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetClientTelemetrySettingsMessage = _reflection.GeneratedProtocolMessageType('GetClientTelemetrySettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETCLIENTTELEMETRYSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.get_client_telemetry_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.GetClientTelemetrySettingsMessage)
  ))
_sym_db.RegisterMessage(GetClientTelemetrySettingsMessage)


# @@protoc_insertion_point(module_scope)
