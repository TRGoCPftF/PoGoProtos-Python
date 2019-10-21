# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/update_player_location_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/update_player_location_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/update_player_location_message.proto\x12\'pogoprotos.networking.requests.messages\"\xa1\x02\n\x1bUpdatePlayerLocationMessage\x12\x1b\n\x13geofence_identifier\x18\x01 \x01(\t\x12_\n\x06reason\x18\x02 \x01(\x0e\x32O.pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage.PingReason\"\x83\x01\n\nPingReason\x12\t\n\x05UNSET\x10\x00\x12\x12\n\x0e\x45NTRANCE_EVENT\x10\x01\x12\x0e\n\nEXIT_EVENT\x10\x02\x12\x0f\n\x0b\x44WELL_EVENT\x10\x03\x12\x0f\n\x0bVISIT_EVENT\x10\x04\x12\x12\n\x0e\x46ITNESS_WAKEUP\x10\x05\x12\x10\n\x0cOTHER_WAKEUP\x10\x06\x62\x06proto3')
)



_UPDATEPLAYERLOCATIONMESSAGE_PINGREASON = _descriptor.EnumDescriptor(
  name='PingReason',
  full_name='pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage.PingReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTRANCE_EVENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT_EVENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DWELL_EVENT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VISIT_EVENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FITNESS_WAKEUP', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER_WAKEUP', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=280,
  serialized_end=411,
)
_sym_db.RegisterEnumDescriptor(_UPDATEPLAYERLOCATIONMESSAGE_PINGREASON)


_UPDATEPLAYERLOCATIONMESSAGE = _descriptor.Descriptor(
  name='UpdatePlayerLocationMessage',
  full_name='pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geofence_identifier', full_name='pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage.geofence_identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage.reason', index=1,
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
    _UPDATEPLAYERLOCATIONMESSAGE_PINGREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=411,
)

_UPDATEPLAYERLOCATIONMESSAGE.fields_by_name['reason'].enum_type = _UPDATEPLAYERLOCATIONMESSAGE_PINGREASON
_UPDATEPLAYERLOCATIONMESSAGE_PINGREASON.containing_type = _UPDATEPLAYERLOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['UpdatePlayerLocationMessage'] = _UPDATEPLAYERLOCATIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdatePlayerLocationMessage = _reflection.GeneratedProtocolMessageType('UpdatePlayerLocationMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEPLAYERLOCATIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.update_player_location_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UpdatePlayerLocationMessage)
  ))
_sym_db.RegisterMessage(UpdatePlayerLocationMessage)


# @@protoc_insertion_point(module_scope)
