# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/opt_out_push_notification_category_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/opt_out_push_notification_category_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nXpogoprotos/networking/platform/requests/opt_out_push_notification_category_message.proto\x12\'pogoprotos.networking.platform.requests\";\n%OptOutPushNotificationCategoryMessage\x12\x12\n\ncategories\x18\x01 \x03(\tb\x06proto3')
)




_OPTOUTPUSHNOTIFICATIONCATEGORYMESSAGE = _descriptor.Descriptor(
  name='OptOutPushNotificationCategoryMessage',
  full_name='pogoprotos.networking.platform.requests.OptOutPushNotificationCategoryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categories', full_name='pogoprotos.networking.platform.requests.OptOutPushNotificationCategoryMessage.categories', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=133,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['OptOutPushNotificationCategoryMessage'] = _OPTOUTPUSHNOTIFICATIONCATEGORYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OptOutPushNotificationCategoryMessage = _reflection.GeneratedProtocolMessageType('OptOutPushNotificationCategoryMessage', (_message.Message,), dict(
  DESCRIPTOR = _OPTOUTPUSHNOTIFICATIONCATEGORYMESSAGE,
  __module__ = 'pogoprotos.networking.platform.requests.opt_out_push_notification_category_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.OptOutPushNotificationCategoryMessage)
  ))
_sym_db.RegisterMessage(OptOutPushNotificationCategoryMessage)


# @@protoc_insertion_point(module_scope)
