# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/client_upgrade_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/client_upgrade_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDpogoprotos/networking/requests/messages/client_upgrade_message.proto\x12\'pogoprotos.networking.requests.messages\"\xeb\x01\n\x14\x43lientUpgradeMessage\x12\x0f\n\x07version\x18\x01 \x01(\t\x12m\n\x10operating_system\x18\x02 \x01(\x0e\x32S.pogoprotos.networking.requests.messages.ClientUpgradeMessage.ClientOperatingSystem\"S\n\x15\x43lientOperatingSystem\x12\x0e\n\nOS_UNKNOWN\x10\x00\x12\x0e\n\nOS_ANDROID\x10\x01\x12\n\n\x06OS_IOS\x10\x02\x12\x0e\n\nOS_DESKTOP\x10\x03\x62\x06proto3')
)



_CLIENTUPGRADEMESSAGE_CLIENTOPERATINGSYSTEM = _descriptor.EnumDescriptor(
  name='ClientOperatingSystem',
  full_name='pogoprotos.networking.requests.messages.ClientUpgradeMessage.ClientOperatingSystem',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS_ANDROID', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS_IOS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS_DESKTOP', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=266,
  serialized_end=349,
)
_sym_db.RegisterEnumDescriptor(_CLIENTUPGRADEMESSAGE_CLIENTOPERATINGSYSTEM)


_CLIENTUPGRADEMESSAGE = _descriptor.Descriptor(
  name='ClientUpgradeMessage',
  full_name='pogoprotos.networking.requests.messages.ClientUpgradeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='pogoprotos.networking.requests.messages.ClientUpgradeMessage.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operating_system', full_name='pogoprotos.networking.requests.messages.ClientUpgradeMessage.operating_system', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTUPGRADEMESSAGE_CLIENTOPERATINGSYSTEM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=349,
)

_CLIENTUPGRADEMESSAGE.fields_by_name['operating_system'].enum_type = _CLIENTUPGRADEMESSAGE_CLIENTOPERATINGSYSTEM
_CLIENTUPGRADEMESSAGE_CLIENTOPERATINGSYSTEM.containing_type = _CLIENTUPGRADEMESSAGE
DESCRIPTOR.message_types_by_name['ClientUpgradeMessage'] = _CLIENTUPGRADEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientUpgradeMessage = _reflection.GeneratedProtocolMessageType('ClientUpgradeMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTUPGRADEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.client_upgrade_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.ClientUpgradeMessage)
  ))
_sym_db.RegisterMessage(ClientUpgradeMessage)


# @@protoc_insertion_point(module_scope)
