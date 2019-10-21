# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/messages/register_push_notification_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/messages/register_push_notification_message.proto',
  package='pogoprotos.networking.social.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nNpogoprotos/networking/social/messages/register_push_notification_message.proto\x12%pogoprotos.networking.social.messages\"\xe9\x02\n\x1fRegisterPushNotificationMessage\x12\x62\n\tapn_token\x18\x01 \x01(\x0b\x32O.pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken\x12\x62\n\tgcm_token\x18\x02 \x01(\x0b\x32O.pogoprotos.networking.social.messages.RegisterPushNotificationMessage.GcmToken\x1aY\n\x08\x41pnToken\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t\x12\x19\n\x11\x62undle_identifier\x18\x02 \x01(\t\x12\x19\n\x11payload_byte_size\x18\x03 \x01(\x05\x1a#\n\x08GcmToken\x12\x17\n\x0fregistration_id\x18\x01 \x01(\tb\x06proto3')
)




_REGISTERPUSHNOTIFICATIONMESSAGE_APNTOKEN = _descriptor.Descriptor(
  name='ApnToken',
  full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_id', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken.registration_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_identifier', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken.bundle_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_byte_size', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken.payload_byte_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=357,
  serialized_end=446,
)

_REGISTERPUSHNOTIFICATIONMESSAGE_GCMTOKEN = _descriptor.Descriptor(
  name='GcmToken',
  full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.GcmToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_id', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.GcmToken.registration_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=448,
  serialized_end=483,
)

_REGISTERPUSHNOTIFICATIONMESSAGE = _descriptor.Descriptor(
  name='RegisterPushNotificationMessage',
  full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apn_token', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.apn_token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcm_token', full_name='pogoprotos.networking.social.messages.RegisterPushNotificationMessage.gcm_token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGISTERPUSHNOTIFICATIONMESSAGE_APNTOKEN, _REGISTERPUSHNOTIFICATIONMESSAGE_GCMTOKEN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=483,
)

_REGISTERPUSHNOTIFICATIONMESSAGE_APNTOKEN.containing_type = _REGISTERPUSHNOTIFICATIONMESSAGE
_REGISTERPUSHNOTIFICATIONMESSAGE_GCMTOKEN.containing_type = _REGISTERPUSHNOTIFICATIONMESSAGE
_REGISTERPUSHNOTIFICATIONMESSAGE.fields_by_name['apn_token'].message_type = _REGISTERPUSHNOTIFICATIONMESSAGE_APNTOKEN
_REGISTERPUSHNOTIFICATIONMESSAGE.fields_by_name['gcm_token'].message_type = _REGISTERPUSHNOTIFICATIONMESSAGE_GCMTOKEN
DESCRIPTOR.message_types_by_name['RegisterPushNotificationMessage'] = _REGISTERPUSHNOTIFICATIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterPushNotificationMessage = _reflection.GeneratedProtocolMessageType('RegisterPushNotificationMessage', (_message.Message,), dict(

  ApnToken = _reflection.GeneratedProtocolMessageType('ApnToken', (_message.Message,), dict(
    DESCRIPTOR = _REGISTERPUSHNOTIFICATIONMESSAGE_APNTOKEN,
    __module__ = 'pogoprotos.networking.social.messages.register_push_notification_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.RegisterPushNotificationMessage.ApnToken)
    ))
  ,

  GcmToken = _reflection.GeneratedProtocolMessageType('GcmToken', (_message.Message,), dict(
    DESCRIPTOR = _REGISTERPUSHNOTIFICATIONMESSAGE_GCMTOKEN,
    __module__ = 'pogoprotos.networking.social.messages.register_push_notification_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.RegisterPushNotificationMessage.GcmToken)
    ))
  ,
  DESCRIPTOR = _REGISTERPUSHNOTIFICATIONMESSAGE,
  __module__ = 'pogoprotos.networking.social.messages.register_push_notification_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.RegisterPushNotificationMessage)
  ))
_sym_db.RegisterMessage(RegisterPushNotificationMessage)
_sym_db.RegisterMessage(RegisterPushNotificationMessage.ApnToken)
_sym_db.RegisterMessage(RegisterPushNotificationMessage.GcmToken)


# @@protoc_insertion_point(module_scope)
