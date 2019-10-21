# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/platform_client_api_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/platform_client_api_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6pogoprotos/settings/platform_client_api_settings.proto\x12\x13pogoprotos.settings\"T\n\x19PlatformClientApiSettings\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\"&\n\x0cSettingsType\x12\r\n\tUNDEFINED\x10\x00\x12\x07\n\x03MAP\x10\x01\x62\x06proto3')
)



_PLATFORMCLIENTAPISETTINGS_SETTINGSTYPE = _descriptor.EnumDescriptor(
  name='SettingsType',
  full_name='pogoprotos.settings.PlatformClientApiSettings.SettingsType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=125,
  serialized_end=163,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMCLIENTAPISETTINGS_SETTINGSTYPE)


_PLATFORMCLIENTAPISETTINGS = _descriptor.Descriptor(
  name='PlatformClientApiSettings',
  full_name='pogoprotos.settings.PlatformClientApiSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.settings.PlatformClientApiSettings.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLATFORMCLIENTAPISETTINGS_SETTINGSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=163,
)

_PLATFORMCLIENTAPISETTINGS_SETTINGSTYPE.containing_type = _PLATFORMCLIENTAPISETTINGS
DESCRIPTOR.message_types_by_name['PlatformClientApiSettings'] = _PLATFORMCLIENTAPISETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformClientApiSettings = _reflection.GeneratedProtocolMessageType('PlatformClientApiSettings', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMCLIENTAPISETTINGS,
  __module__ = 'pogoprotos.settings.platform_client_api_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.PlatformClientApiSettings)
  ))
_sym_db.RegisterMessage(PlatformClientApiSettings)


# @@protoc_insertion_point(module_scope)
